from .models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Question
    fields = ('content', 'order_id', 'question_type', 'q_id', 'rev', 'short')