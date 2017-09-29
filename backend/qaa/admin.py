from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Choice

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('content', 'q_id', 'short')

class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('id', 'content', 'order_id' ,'group_id',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Choice, ChoiceAdmin)