from staticjinja import Site
import os


members = {
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

if __name__ == "__main__":
    PROJECT_PATH = "./projects/"
    projects = []
    for fn in os.listdir(PROJECT_PATH):
        with open(os.path.join(PROJECT_PATH, fn)) as f:
            # text = f.read()
            lines = f.readlines()
            if len(lines) == 0:
                continue

            # lines = text.split("\n")

            projects.append({
                'title': lines[0].lstrip("#").strip(),
                'tags': lines[2].lstrip("Tags:").strip().split(),
                'description': "\n".join([l.strip() for l in lines[4:] if len(l.strip()) > 0]),
            })
            print(projects[-1])

    # print(projects)
    site = Site.make_site(
        outpath="docs", extensions=['jinja_markdown.MarkdownExtension'],
        contexts=[('about.html', members), ('index.html', {'projects': projects})]
    )
    # enable automatic reloading
    site.render(use_reloader=True)
