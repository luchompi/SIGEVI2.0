from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class index(LoginRequiredMixin,TemplateView):
    template_name = "Home/index.html"


class not_found(TemplateView):
    template_name = "Home/404.html"


class forbidden(TemplateView):
    template_name = "Home/403.html"
