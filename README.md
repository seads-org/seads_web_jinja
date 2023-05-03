# SEADS website

The website is written in HTML with Bootstrap for styles and [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/) (pythonic syntax for HTML generation, which is used in Django and Flask). It uses [staticjinja](https://github.com/staticjinja/staticjinja) to compile all Jinja templates into static HTMLs and [jinja-markdown](https://github.com/jpsca/jinja-markdown) to allow for markdown entries. The `docs` folder is generated automatically and should not be edited, with all code being located in the `templates` folder.

## Deployment

To use it, install dependencies first:

```
mamba env create -f ./environment.yml --prefix ./env
npm install
```

To produce `docs`:

```
./env/bin/python build.py
```

To run dev server:
```
./env/bin/python build.py dev
```

## Adding project descriptions

All project info is contained in the [`./projects`](./projects) folder. Empty markdown files are ignored. The second line should contain tags (example [here](./projects/01_gwwc_network.md)), which are not used for now but will be rendered in the future.