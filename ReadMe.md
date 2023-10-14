[![tests](https://img.shields.io/badge/tests-passing-brightgreen)]() [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Django App Skeleton

This repository serves as a starting point or template for new Django apps, providing common dependencies and settings.

## Dependencies

[![django](https://img.shields.io/badge/django-v4.2.1-green)](https://www.djangoproject.com/start/overview/)

[![django-browser-reload](https://img.shields.io/badge/django--browser--reload-v1.12.0-yellowgreen)](https://github.com/adamchainz/django-browser-reload)

[![django-debug-toolbar](https://img.shields.io/badge/django--debug--toolbar-v4.2.0-blue)](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)

[![python-dotenv](https://img.shields.io/badge/python--dotenv-v1.0.0-orange)](https://pypi.org/project/python-dotenv/)

[![ruff](https://img.shields.io/badge/ruff-v0.0.292-orange)](https://docs.astral.sh/ruff/)

## Usage

To use this repo

### Clone or Fork

```bash
    $ git clone https://github.com/TrippleA-Ashaba/django-app-skeleton.git
    $ cd django-skeleton-app

```

### Create a Virtual Environment

```bash
    # windows
    $ python -m venv .venv
    $ source .venv/Scripts/activate
```

```bash
    # unix
    $ python3 -m venv .venv
    $ source .venv/bin/activate
```

### Install dependencies

```bash
    $ pip install -r requirements.txt
```

### Add Environment variables

create a `.env` file and add variables from `sample.env`.

### Runserver

```bash
    $ python manage.py runserver

    #visit 127.0.0.1:8000
```

### Enjoy!!!
