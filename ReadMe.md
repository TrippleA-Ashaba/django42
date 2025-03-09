[![tests](https://img.shields.io/badge/tests-passing-brightgreen)]() [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Django42 (A Skeleton Template of Your Needs)

This repository serves as a starting point or template for new Django apps, providing common dependencies and settings.

## Dependencies

[![django](https://img.shields.io/badge/django-v5.1.7-green)](https://www.djangoproject.com/start/overview/)

## Usage

To use this repo

### Clone or Fork

```bash
    $ git clone https://github.com/TrippleA-Ashaba/django42.git
    $ cd django42

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
    $ pip install pipenv
    $ pipenv install --dev
```

### Add Environment variables

create a `.env` file and add variables from `sample.env`.

### Runserver

```bash
    $ python manage.py runserver

    #visit 127.0.0.1:8000
```

### Enjoy!!!
