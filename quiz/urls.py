from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('',views.homepage),
    path('start_quiz',views.start_quiz, name='start_quiz'),
    path('quiz',views.quiz, name='quiz'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)