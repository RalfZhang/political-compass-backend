from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
  questions = Question.objects
  output = ', '.join(p.short for p in questions)
  return HttpResponse(output)
# def questions(request):
#   return 'hello'