from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('',views.homepage),
    path('quiz',views.quiz, name='quiz'),
    path('leaderboard',views.leaderboard, name = 'leaderboard'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)