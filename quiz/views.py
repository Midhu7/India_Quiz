from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'quiz/homepage.html')

def start_quiz(request):
    return render(request, 'quiz/start_quiz.html')

@login_required(login_url = "accounts:login")
def quiz(request):
    return render(request, 'quiz/quiz.html')
