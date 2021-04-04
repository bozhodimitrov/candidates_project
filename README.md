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
