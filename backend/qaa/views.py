from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import viewsets
import json

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
  if request.method == 'GET':
    return HttpResponse("GEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEET")
  elif request.method == 'POST':
    return HttpResponse('POOOOOOOOOOOOOOOOOOOOOOOOOOOOOOST')
  return HttpResponse('unknown method')

# 获取问题列表
def getQuestionList(request):
  questions = Question.objects.all().order_by('order_id')
  # todo 优化为 lambda exp
  questionList = []
  for item in questions:
    questionList.append(item.toDict())
  allJson = json.dumps(questionList)
  return HttpResponse(allJson)

# 获取单个问题
def getQuestionById(request, question_id):
  id = int(question_id)
  question = Question.objects.get(id=id)
  resJson = json.dumps(question.toDict())
  return HttpResponse(resJson)

# 提交答案
def postAnswer(request):
  # 非 post 即返回
  if request.method != 'POST':
    return Http404('')
  # request.params
  return HttpResponse('test')

def statsQuestionDistribution(request):
  id=int(123)
  if id:
    question = Question.objects.get(id=id)
    q_id = question.q_id
    # //todo
  return