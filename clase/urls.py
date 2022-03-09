from django.contrib import admin
from django.urls import path,include
from . views import nuevoCurso

urlpatterns = [
    path('c/',nuevoCurso,name='nuevo_curso'),
    path('admin/', admin.site.urls),
]    