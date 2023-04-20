# SEADS website

The website is written in HTML with Bootstrap for styles and [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) (pythonic syntax for HTML generation, which is used in Django and Flask). It uses [staticjinja](https://github.com/staticjinja/staticjinja) to compile all Jinja templates into static HTMLs and [jinja-markdown](https://github.com/jpsca/jinja-markdown) to allow for markdown entries. The `docs` folder is generated automatically and should not be edited, with all code being located in the `templates` folder.

To use it, install dependencies first:

```
pip install staticjinja jinja-markdown watchdog libsass
npm install
```

To to produce `docs`:

```
python build.py
```

To run dev server:
```
python build.py dev
```
