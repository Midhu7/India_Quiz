from django.contrib import admin
from .models import Question, Attempt, Highscore, Answer

admin.site.register(Question)
admin.site.register(Attempt)
admin.site.register(Highscore)
admin.site.register(Answer)
