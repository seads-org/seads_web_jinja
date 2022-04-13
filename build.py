from staticjinja import Site


if __name__ == "__main__":
    site = Site.make_site(outpath="public", extensions=['jinja_markdown.MarkdownExtension'])
    # enable automatic reloading
    site.render(use_reloader=True)