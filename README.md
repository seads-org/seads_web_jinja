# SEADS website

The website is written in HTML with [Bulma](https://bulma.io/documentation/) for styles (it's like bootstrap for kids) and [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) (pythonic syntax for HTML generation, which is used in Django and Flask). It uses [staticjinja](https://github.com/staticjinja/staticjinja) to compile all Jinja templates into static HTMLs and [jinja-markdown](https://github.com/jpsca/jinja-markdown) to allow for markdown entries. The `docs` folder is generated automatically and should not be edited, with all code being located in the `templates` folder.

To use it, install dependencies first:
```
pip install staticjinja jinja-markdown watchdog libsass
npm install
```

And then build it to produce `docs` HTMLs:

```
python build.py
```

To serve them locally (e.g., for testing purposes), you can use python server:
```
cd docs
python -m http.server 8000
```
