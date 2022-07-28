from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Question, Attempt, Highscore, Answer
from random import sample

def homepage(request):
    return render(request, 'quiz/homepage.html')

def start_quiz(request):
    return render(request, 'quiz/start_quiz.html')

def leaderboard(request):
    data = Highscore.objects.all()
    return render(request, 'quiz/leaderboard.html',{'data':data})

@login_required(login_url = "accounts:login")
def quiz(request):
    if request.method == 'GET':
        n = Question.objects.all().count()
        questions = []
        indices = sample(range(0,n-1),5)
        for i in indices:
            questions.append(Question.objects.all()[i])
        print(questions)
        return render(request, 'quiz/quiz.html', {'questions':questions})
    else:
        attempt = Attempt()
        attempt.no_of_correct_answers = 0
        attempt.no_of_wrong_answers = 0
        print(request.POST)
        for (key,value) in request.POST.items():
            if(key != 'csrfmiddlewaretoken'):
                q = Answer.objects.filter(question_id = key)[0]
                if q.correct_answer == value:
                    attempt.no_of_correct_answers += 1
                else:
                    attempt.no_of_wrong_answers += 1
        attempt.score = attempt.no_of_correct_answers*4+attempt.no_of_wrong_answers*-1
        attempt.user = request.user
        attempt.save()
        queryset = Highscore.objects.filter(user = request.user)
        is_new_highscore = False
        if(queryset.exists()):
            topscore = queryset[0]
            if attempt.score > topscore.highscore:
                is_new_highscore = True
                topscore.highscore = attempt.score
                topscore.save()
        else:
            topscore = Highscore()
            topscore.user = request.user
            topscore.highscore = attempt.score
            is_new_highscore = True
            topscore.save()
        return render(request, 'quiz/result.html',{'attempt': attempt, 'is_new_highscore': is_new_highscore})