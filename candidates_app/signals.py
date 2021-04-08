from django.db.models.signals import post_save
from django.dispatch import receiver

from candidates_app.models import Score


@receiver(post_save, sender=Score)
def new_score(sender, **kwargs):
    score = kwargs['instance']
    print(f'New score {score} for {score.candidate}')
