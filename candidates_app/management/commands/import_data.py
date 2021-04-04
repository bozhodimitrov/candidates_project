import contextlib
import csv
import os

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.db import transaction

from candidates_app.models import Candidate
from candidates_app.models import Score


DEFAULT_FILENAME = 'candidates.csv'


class Command(BaseCommand):
    help = 'Import data from different file formats into databse'

    def add_arguments(self, parser):
        parser.add_argument(
            'source_file',
            default=DEFAULT_FILENAME,
            help=f'source file containing data (default: {DEFAULT_FILENAME})',
            nargs='?',
            type=str,
        )

    def handle(self, *args, **options):
        filename, ext = os.path.splitext(options['source_file'])
        if ext.endswith('csv'):
            self.import_csv(options['source_file'])
        else:
            raise CommandError('Unsupported file format')

    def import_csv(self, csv_file):
        with open(csv_file) as f:
            reader = csv.DictReader(f)
            for record in reader:
                with contextlib.suppress(ValidationError, ValueError):
                    with transaction.atomic():
                        Candidate(
                            name=record['name'],
                            reference_code=record['candidate_ref'],
                        ).clean_fields()
                        candidate, _ = Candidate.objects.get_or_create(
                            name=record['name'],
                            reference_code=record['candidate_ref'],
                        )

                        score = Score(
                            candidate=candidate,
                            value=float(record['score']),
                        )
                        score.clean_fields()
                        score.save()
