from django.shortcuts import render

from candidates_app.models import Candidate
from candidates_app.models import Score


def candidates(request):
    candidates = Candidate.objects.order_by('name').all()
    if candidates:
        best_candidate = Score.objects.latest('value').candidate
    else:
        best_candidate = None

    context = {'candidates': candidates, 'best_candidate': best_candidate}
    return render(request, 'candidates_app/index.html', context)
