from .models import Question, Answer, Choice
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  # choice = ChoiceSerializer()
  class Meta:
    model = Question
    fields = ('id', 'content', 'order_id', 'question_type', 'q_id', 'rev', 'short', 'choice_group')

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Choice
    fields = ('content', 'value', 'order_id', 'group_id')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
  class Meta: 
    model = Answer
    fields = ('time', 'q101', 'q102', 'q104', 'q103', 'q106', 'q105', 'q107', 'q108', 'q109', 'q111', 'q110', 'q112', 'q113', 'q114', 'q115', 'q117', 'q119', 'q116', 'q120', 'q118', 'q301', 'q302', 'q303', 'q304', 'q305', 'q306', 'q309', 'q307', 'q308', 'q310', 'q311', 'q312', 'q313', 'q314', 'q316', 'q317', 'q318', 'q319', 'q320', 'q315', 'q201', 'q202', 'q203', 'q204', 'q205', 'q206', 'q207', 'q208', 'q209', 'q210', 'q1001', 'q1002', 'q1003', 'q1004', 'ip', 'device', 'add')