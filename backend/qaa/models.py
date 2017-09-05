import datetime

# Create your models here.

from django.db import models
from django.utils import timezone

class Choice(models.Model):
  content = models.CharField(max_length=255)
  # question_id = models.ForeignKey(Question)
  value = models.IntegerField()
  order_id = models.IntegerField()

class Question(models.Model):
  content = models.CharField(max_length=255)
  order_id = models.IntegerField()
  question_type = models.IntegerField()
  addtion = models.CharField(max_length=50)
  q_id = models.CharField(max_length=50)
  rev = models.IntegerField()
  short = models.CharField(max_length=50)
  choice = models.ForeignKey(Choice)
  def __str__(self):
    if self.short:
      return self.short
    else: 
      return self.content

class Answer(models.Model):
  time = models.DateTimeField()
  add = models.CharField(max_length=50, null=True, blank=True)
  q101 = models.IntegerField(null=True, blank=True)
  q102 = models.IntegerField(null=True, blank=True)
  q104 = models.IntegerField(null=True, blank=True)
  q103 = models.IntegerField(null=True, blank=True)
  q106 = models.IntegerField(null=True, blank=True)
  q105 = models.IntegerField(null=True, blank=True)
  q107 = models.IntegerField(null=True, blank=True)
  q108 = models.IntegerField(null=True, blank=True)
  q109 = models.IntegerField(null=True, blank=True)
  q111 = models.IntegerField(null=True, blank=True)
  q110 = models.IntegerField(null=True, blank=True)
  q112 = models.IntegerField(null=True, blank=True)
  q113 = models.IntegerField(null=True, blank=True)
  q114 = models.IntegerField(null=True, blank=True)
  q115 = models.IntegerField(null=True, blank=True)
  q117 = models.IntegerField(null=True, blank=True)
  q119 = models.IntegerField(null=True, blank=True)
  q116 = models.IntegerField(null=True, blank=True)
  q120 = models.IntegerField(null=True, blank=True)
  q118 = models.IntegerField(null=True, blank=True)
  q301 = models.IntegerField(null=True, blank=True)
  q302 = models.IntegerField(null=True, blank=True)
  q303 = models.IntegerField(null=True, blank=True)
  q304 = models.IntegerField(null=True, blank=True)
  q305 = models.IntegerField(null=True, blank=True)
  q306 = models.IntegerField(null=True, blank=True)
  q309 = models.IntegerField(null=True, blank=True)
  q307 = models.IntegerField(null=True, blank=True)
  q308 = models.IntegerField(null=True, blank=True)
  q310 = models.IntegerField(null=True, blank=True)
  q311 = models.IntegerField(null=True, blank=True)
  q312 = models.IntegerField(null=True, blank=True)
  q313 = models.IntegerField(null=True, blank=True)
  q314 = models.IntegerField(null=True, blank=True)
  q316 = models.IntegerField(null=True, blank=True)
  q317 = models.IntegerField(null=True, blank=True)
  q318 = models.IntegerField(null=True, blank=True)
  q319 = models.IntegerField(null=True, blank=True)
  q320 = models.IntegerField(null=True, blank=True)
  q315 = models.IntegerField(null=True, blank=True)
  q201 = models.IntegerField(null=True, blank=True)
  q202 = models.IntegerField(null=True, blank=True)
  q203 = models.IntegerField(null=True, blank=True)
  q204 = models.IntegerField(null=True, blank=True)
  q205 = models.IntegerField(null=True, blank=True)
  q206 = models.IntegerField(null=True, blank=True)
  q207 = models.IntegerField(null=True, blank=True)
  q208 = models.IntegerField(null=True, blank=True)
  q209 = models.IntegerField(null=True, blank=True)
  q210 = models.IntegerField(null=True, blank=True)
  q1001 = models.CharField(max_length=255, blank=True)
  q1002 = models.CharField(max_length=255, blank=True)
  q1003 = models.CharField(max_length=255, blank=True)
  q1004 = models.CharField(max_length=255, blank=True)
  ip = models.CharField(max_length=255, blank=True)
  device = models.CharField(max_length=255, blank=True)
