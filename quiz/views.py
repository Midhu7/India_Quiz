from django.shortcuts import render

def homepage(request):
    return render(request, 'quiz/homepage.html')

def start_quiz(request):
    return render(request, 'quiz/start_quiz.html')

def quiz(request):
    return render(request, 'quiz/quiz.html')
