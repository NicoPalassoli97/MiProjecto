
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('cu/',include("clase.urls")),
    path('',include("indice.urls")),
    path('admin/', admin.site.urls),
    
]
