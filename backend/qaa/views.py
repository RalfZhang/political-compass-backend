from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all().order_by('order_id')
  serializer_class = QuestionSerializer
  http_method_names = ['get', 'head']

class AnswerViewSet(viewsets.ModelViewSet):
  queryset = Answer.objects.all().order_by('id')
  serializer_class = AnswerSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def questions(request):
  questions = Question.objects.all()
  output = ', '.join(p.__str__() for p in questions)
  return HttpResponse(output)
def question(request, question_id):
  id = int(question_id)
  question = Question.objects.get(id=id)
  return HttpResponse(question.__str__())