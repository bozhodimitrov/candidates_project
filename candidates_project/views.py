from django.shortcuts import render


def index(request):
    return render(request, 'candidates_project/index.html')
