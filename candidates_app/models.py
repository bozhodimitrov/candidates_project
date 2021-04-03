from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from candidates_app.validators import reference_code_validator


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    reference_code = models.CharField(
        max_length=8,
        validators=[reference_code_validator],
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'reference_code'],
                name='unique candidate',
            ),
        ]

    def __str__(self):
        return f'{self.name} ({self.reference_code})'


class Score(models.Model):
    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        related_name='scores',
    )

    value = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
    )

    def __str__(self):
        return f'{self.value}'
