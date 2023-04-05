import staticjinja
import os, os.path, threading
import watchdog.events, watchdog.observers
import sass

ROOTS = ['about.html', 'contact.html', 'index.html']

def observe(path, on_change):
    class Handler(watchdog.events.FileSystemEventHandler):
        def on_any_event(self, event):
            on_change()

    observer = watchdog.observers.Observer()
    observer.schedule(Handler(), path, recursive=True)
    observer.start()
    return observer


def debounce(wait_time):
    def decorator(function):
        def debounced(*args, **kwargs):
            def call_function():
                debounced._timer = None
                return function(*args, **kwargs)
            if debounced._timer is not None:
                debounced._timer.cancel()
            debounced._timer = threading.Timer(wait_time, call_function)
            debounced._timer.start()
        debounced._timer = None
        return debounced
    return decorator



# Config

def read_members():
    return {
        'members': [
            {
                'name': 'Viktor Petukhov', 'location': 'Tbilisi, Georgia', 'url': 'https://www.linkedin.com/in/v-petukhov',
                'bio': 'Viktor holds a PhD in Biostatistics from the University of Copenhagen. His main focus is on interpretable data analysis and statistical modeling. Having experience in academic research and for-profit AI consulting, he is now shifting towards providing infrastructure for new EA organizations.'
            },
            {
                'name': 'Jaime Raldua Veuthey', 'location': 'Munich, Germany', 'url': 'https://www.linkedin.com/in/jaime-raldua-veuthey-0473aa64/',
                'bio': 'Jaime is a Software Developer with background in Industrial and Mechanical Engineering. With 5+ years of experience in the Robotics and Railway Industry his main focus at the moment is Data Science. With a tech focus on the architecture and MLOps, he is focusing on supporting EA groups and improving the EA infrastructure.'
            },
            {
                'name': 'Georg Wind', 'location': 'Konstanz, Germany', 'url': 'https://www.linkedin.com/in/georg-wind/',
                'bio': 'Georg is pursuing a master&rsquo;s degree in Social and Economic Data Science from the University of Konstanz and holds a BA in Philosophy &amp; Economics from the University of Bayreuth. He has several years of experience in strategy development, operational management, and partnerships development for various NPOs.'
            },
            # {
            #     'name': '', 'location': '', 'url': '',
            #     'bio': ''
            # },
        ],
        'past_members': [
            {
                'name': 'Severin Trösch', 'location': 'Bern, Switzerland', 'url': 'https://www.linkedin.com/in/severin-tr%C3%B6sch-0a8a37103/',
                'bio': 'Senior Data Scientist at Datahouse AG. Severin came up with the original idea of SEADS.'
            },
            {
                'name': 'Elena Plekhanova', 'location': 'Tbilisi, Georgia', 'url': 'https://www.linkedin.com/in/elena-plekhanova-9367a910a/',
                'bio': "Elena holds a PhD in Ecology from the University of Zurich. She's an expert in analysis of ecological data."
            },
            {
                'name': 'David Marti', 'location': 'Basel, Switzerland', 'url': 'https://www.linkedin.com/in/david-b-marti/',
                'bio': 'Programme Officer at a science & technology think tank Pour Demain'
            },
        ]
    }

def read_projects(path):
    projects = []
    for fn in os.listdir(path):
        with open(os.path.join(path, fn)) as f:
            lines = f.readlines()
            if len(lines) == 0:
                continue

            projects.append({
                'title': lines[0].lstrip("#").strip(),
                'tags': lines[2].lstrip("Tags:").strip().split(),
                'description': "\n".join([l.strip() for l in lines[4:] if len(l.strip()) > 0]),
            })
    return projects

def build_styles(path):
    with open("./docs/styles.css", "w") as file:
        file.write(sass.compile(filename = os.path.join(path, "styles.scss")))

def build_html(site, members, projects):
    site.contexts = [('about.html', members), ('index.html', {'projects': projects})]
    site.render()

class Site(staticjinja.Site):
    def is_template(self, template):
        return template in ROOTS

def main():
    PROJECTS  = "./projects/"
    STYLES    = './styles/'
    TEMPLATES = './templates'

    members = read_members()
    projects = read_projects(PROJECTS)
    build_styles(STYLES)

    site = Site.make_site(outpath="docs", extensions=['jinja_markdown.MarkdownExtension'], contexts=[])
    build_html(site, members, projects)

    @debounce(0.1)
    def on_styles_change():
        print("Rebuilding styles (styles changed)")
        build_styles(STYLES)

    @debounce(0.1)
    def on_projects_change():
        print("Rebuilding htmls (data changed)")
        nonlocal projects
        projects = read_projects(PROJECTS)
        build_html(site, members, projects)

    @debounce(0.1)
    def on_templates_change():
        print("Rebuilding htmls (templates changed)")
        build_html(site, members, projects)


    observers = [
        observe(STYLES,    on_styles_change),
        observe(PROJECTS,  on_projects_change),
        observe(TEMPLATES, on_templates_change),
    ]

    try:
        while all(o.is_alive() for o in observers):
            for observer in observers:
                observer.join(1)
    finally:
        for observer in observers:
            observer.stop()
            observer.join()

if __name__ == "__main__":
    main()