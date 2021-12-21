from django.urls import path 
from . import views as v

urlpatterns = [
    path('',v.index.as_view()),
    path('403/',v.forbidden.as_view()),
    path('404/',v.not_found.as_view()),


]
