from django.shortcuts import render


def candidates(request):
    return render(request, 'candidates_app/index.html')
