from django.db import models
from django.contrib.auth.models import User

answer_options = (
    (1,'option 1'),
    (2,'option 2'),
    (3,'option 3'),
    (4,'option 4'),
)

class Question(models.Model):
    question = models.TextField(max_length = 1000, default="Question")
    option1 = models.CharField(max_length = 100, null = True)
    option2 = models.CharField(max_length = 100, null = True)
    option3 = models.CharField(max_length = 100, null = True)
    option4 = models.CharField(max_length = 100, null = True)
    answer = models.IntegerField(choices = answer_options, null = True)

    def __str__(self):
        return self.question

class Attempt(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    no_of_correct_answers = models.IntegerField(default = 0)
    no_of_wrong_answrs = models.IntegerField(default = 0)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return self.score

class Highscore(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    highscore = models.IntegerField(default = 0)

    def __str__(self):
        return self.highscore