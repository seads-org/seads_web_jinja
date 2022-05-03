# SEADS web-site

The web-site is written on html with [Bulma](https://bulma.io/documentation/) for styles (it's like bootstrap for kids) and [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) (pythonic syntax for html generation, which is used in Django and Flask). It uses [staticjinja](https://github.com/staticjinja/staticjinja) to compile all Jinja templates into static htmls and [jinja-markdown](https://github.com/jpsca/jinja-markdown) to allow for markdown entries. The `docs` folder is generated automatically and should not be edited, with all code being located in the `templates` folder.

To use it, install dependencies first:
```
pip install staticjinja jinja-markdown
```

And then build it to produce `docs` htmls:

```
python build.py
cp -r static docs
```

To serve them locally (e.g., for testing purposes), you can use python server:
```
cd docs
python -m http.server 8000
```
