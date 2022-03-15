from django.urls import path
from .views import inicio,another_view, numero_random, numero_,mi_plantilla    
    
    
urlpatterns =  [    
    path('',inicio),
    path('otra-vista/',another_view),
    path('r/',numero_random),
    path('n/<int:numero>',numero_),
    path('mp/',mi_plantilla),
    
]    