# Template for LinkML schema repos

## What is this?

This is a templated repository for Alliance of Genome Resources Persistent schema.  It takes care of generating a readthedocs themed
site, as well as downstream artefacts, including:

 * JSON-Schema
 * ShEx
 * OWL
 * RDF (direct mapping)
 * SQL DDL (TODO)
 * TSV/CSV reports

## Quickstart

 1. Make a branch off main 
 2. Type `make install all alliance-schema.yaml` to build your downstream artefacts (jsonschema, owl, etc)
 3. Type `make gh-deploy` to make a github pages website

Minor tweak: for now you must pass in the name of your schema on the command line, e.g.

```bash
make clean
mkdir target
make all alliance-schema.yaml
```


To view a copy of your UML and documentation locally:
```
mkdocs serve
```
Use the URL that command provides to visit your local documentation/changes.

## How it works

This repo is a GitHub "template" repo. When you "Use this template" it will make a copy for your project.

Everything is orchestrated by a generic single [Makefile](Makefile). For this to work you should follow certain conventions:

 * Keep your schema in src/schema
 * Use the `.yaml` suffix for all schema files
 * Use the suggested directory layout here.

To run the Makefile you will need Python (>=3.7), and biolinkml. You can type:

```bash
make install
```

or equivalently

```bash
. environment.sh
pip install -r requirements.txt
```

You can make specific targets, e.g

```bash
make stage-jsonschema
```

Use the `all` target to make everything

Note to redeploy documentation all you need to do is:

```bash
make gh-deploy
```

That's it!

The Makefile takes care of dependencies. Downstream files are only rebuilt if source files change.

## Documentation framework

You can change the theme by editing [mkdocs.yml](mkdocs.yml)

Do not edit docs in place. They are placed in the `docs` dir by `make stage-docs`.

You can add your own docs to `src/docs/

Note that docs are actually deployed on the gh-pages branch, but you don't need to worry about this. Just type:

```bash
make gh-deploy
```

The template site is deployed on

http://cmungall.github.io/linkml-template

But this is not very interesting as it is a toy schema
