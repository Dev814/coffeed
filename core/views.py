from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

# classed baseed view

class SplashView(TemplateView):
  template_name = "index.html"

