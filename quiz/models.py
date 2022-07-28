from django.db import models
from django.contrib.auth.models import User
import uuid



class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    question = models.TextField(max_length = 1000, default="Question")
    option1 = models.CharField(max_length = 100, null = True)
    option2 = models.CharField(max_length = 100, null = True)
    option3 = models.CharField(max_length = 100, null = True)
    option4 = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    correct_answer = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.correct_answer

class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    submission_date_and_time = models.DateField(auto_now_add=True)
    no_of_correct_answers = models.IntegerField(default = 0)
    no_of_wrong_answers = models.IntegerField(default = 0)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username

class Highscore(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    highscore = models.IntegerField(default = 0)

    def __str__(self):
        return self.user.username