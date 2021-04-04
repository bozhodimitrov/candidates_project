import contextlib
import csv
import json
import os

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError


CSV_COLUMNS = ('candidate_ref', 'name', 'score')

SOURCE_FILENAME = 'candidates.json'
OUTPUT_FILENAME = 'candidates.csv'


class Command(BaseCommand):
    help = 'Convert source file into different file format and sort the data'

    def add_arguments(self, parser):
        parser.add_argument(
            'source_file',
            default=SOURCE_FILENAME,
            help=f'source file containing data (default: {SOURCE_FILENAME})',
            nargs='?',
            type=str,
        )

        parser.add_argument(
            '-o',
            '--output-file',
            default=OUTPUT_FILENAME,
            help=f'output file for storing data (default: {OUTPUT_FILENAME})',
            type=str,
        )

    def handle(self, *args, **options):
        if not os.path.isfile(options['source_file']):
            raise CommandError(f"Invalid file: {options['source_file']}")

        src_filename, src_ext = os.path.splitext(options['source_file'])
        out_filename, out_ext = os.path.splitext(options['output_file'])

        if src_ext.endswith('json') and out_ext.endswith('.csv'):
            self.json_to_csv(options['source_file'], options['output_file'])
        else:
            raise CommandError('Unsupported file format')

    def json_to_csv(self, source_file, output_file):
        with open(source_file) as f:
            candidates = json.load(f)

        candidates.sort(key=lambda candidate: candidate['score'])

        with open(output_file, mode='w', newline='') as f:
            writer = csv.DictWriter(
                f,
                fieldnames=CSV_COLUMNS,
                lineterminator='\n',
            )
            writer.writeheader()

            for candidate in candidates:
                with contextlib.suppress(ValueError):
                    writer.writerow(candidate)
