from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from quiz import views as quiz_views

urlpatterns = [
    path('',quiz_views.homepage, name="home"),
    path('quiz/', include('quiz.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)