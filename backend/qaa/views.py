from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
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
  try:
    answer = Answer(time = timezone.now(), q101 = int(request.POST['q101']), q102 = int(request.POST['q102']), q104 = int(request.POST['q104']), q103 = int(request.POST['q103']), q106 = int(request.POST['q106']), q105 = int(request.POST['q105']), q107 = int(request.POST['q107']), q108 = int(request.POST['q108']), q109 = int(request.POST['q109']), q111 = int(request.POST['q111']), q110 = int(request.POST['q110']), q112 = int(request.POST['q112']), q113 = int(request.POST['q113']), q114 = int(request.POST['q114']), q115 = int(request.POST['q115']), q117 = int(request.POST['q117']), q119 = int(request.POST['q119']), q116 = int(request.POST['q116']), q120 = int(request.POST['q120']), q118 = int(request.POST['q118']), q301 = int(request.POST['q301']), q302 = int(request.POST['q302']), q303 = int(request.POST['q303']), q304 = int(request.POST['q304']), q305 = int(request.POST['q305']), q306 = int(request.POST['q306']), q309 = int(request.POST['q309']), q307 = int(request.POST['q307']), q308 = int(request.POST['q308']), q310 = int(request.POST['q310']), q311 = int(request.POST['q311']), q312 = int(request.POST['q312']), q313 = int(request.POST['q313']), q314 = int(request.POST['q314']), q316 = int(request.POST['q316']), q317 = int(request.POST['q317']), q318 = int(request.POST['q318']), q319 = int(request.POST['q319']), q320 = int(request.POST['q320']), q315 = int(request.POST['q315']), q201 = int(request.POST['q201']), q202 = int(request.POST['q202']), q203 = int(request.POST['q203']), q204 = int(request.POST['q204']), q205 = int(request.POST['q205']), q206 = int(request.POST['q206']), q207 = int(request.POST['q207']), q208 = int(request.POST['q208']), q209 = int(request.POST['q209']), q210 = int(request.POST['q210']), q1001 = int(request.POST['q1001']), q1002 = int(request.POST['q1002']), q1003 = int(request.POST['q1003']), q1004 = int(request.POST['q1004']), ip = '123', device = 'ddddmode')
    answer.save()
  except Exception:
    return HttpResponse('error')
  return HttpResponse('ok')

def statsQuestionDistribution(request):
  id=int(123)
  if id:
    question = Question.objects.get(id=id)
    q_id = question.q_id
    # //todo
  return