from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import Question, Answer, Choice
from .serializers import QuestionSerializer, AnswerSerializer, ChoiceSerializer

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all().order_by('order_id')
  serializer_class = QuestionSerializer
  http_method_names = ['get', 'head']

class ChoiceViewSet(viewsets.ModelViewSet): 
  queryset = Choice.objects.all().order_by('order_id')
  serializer_class = ChoiceSerializer
  http_method_names = ['get', 'head']

class AnswerViewSet(viewsets.ModelViewSet):
  queryset = Answer.objects.all().order_by('id')
  serializer_class = AnswerSerializer
  http_method_names = ['post']

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def questions(request):
  if question.param.question_id not None:
    questions = Question.objects.all()
    output = ', '.join(p.__str__() for p in questions)
    return HttpResponse(output)
  else:
    questions = Question.objects.filter(id = question.param.question_id)
    output = ', '.join(p.__str__() for p in questions)
    return HttpResponse(output)
def question(request, question_id):
  id = int(question_id)
  question = Question.objects.get(id=id)
  return HttpResponse(question.__str__())

def statsQuestionDistribution(request):
  id=int(123)
  if id:
    question = Question.objects.get(id=id)
    q_id = question.q_id
    # //todo
  return