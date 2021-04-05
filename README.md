# Candidates project

Example application for listing candidate scores based on Django web framework.

## Development

Setup for running the development server and management commands:

```bash
python manage.py runserver --settings=candidates_project.dev_settings
# OR
DJANGO_SETTINGS_MODULE='candidates_project.dev_settings'
python manage.py runserver
```

## Management commands

Import data into database from source files.
Supported source formats: `csv`

```bash
python manage.py import_data --help
python manage.py import_data
python manage.py import_data <source_filename>
```

Convert data from one source file into another.
Supported conversions: `json` -> `csv`

```bash
python manage.py convert_data --help
python manage.py convert_data
python manage.py convert_data <source_filename> <output_filename>
```

## List of online docs and resources

I used the following list of resources as a reference:

- Django
  - [Quick Guide and Tutorial](https://docs.djangoproject.com/en/3.1/intro/install/)
  - [Models](https://docs.djangoproject.com/en/3.1/ref/models/instances/)
  - [Model fields](https://docs.djangoproject.com/en/3.1/ref/models/fields/)
  - [Many-to-one](https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/)
  - [Database transactions](https://docs.djangoproject.com/en/3.1/topics/db/transactions/)
  - [URL dispatcher](https://docs.djangoproject.com/en/3.1/topics/http/urls/)
  - [Built-in template tags and filters](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/)
  - [Validators](https://docs.djangoproject.com/en/3.1/ref/validators/)
  - [Custom management commands](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/)
  - [Signals](https://docs.djangoproject.com/en/3.1/topics/signals/)
- Python
  - [json](https://docs.python.org/3/library/json.html)
  - [csv](https://docs.python.org/3/library/csv.html)
- [Anatomy of an HTML document](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document)
