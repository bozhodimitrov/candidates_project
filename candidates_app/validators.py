import string

from django.core.exceptions import ValidationError


ALLOWED_REFERENCE_CHARS = frozenset(string.printable[:62])


def reference_code_validator(value):
    if len(value) != 8:
        raise ValidationError('Invalid reference code length')

    if any(ch not in ALLOWED_REFERENCE_CHARS for ch in value):
        raise ValidationError('Invalid reference code format')
