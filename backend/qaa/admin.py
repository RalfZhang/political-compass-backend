from django.contrib import admin

# Register your models here.
from .models import Question, Answer, Choice

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('q_id', 'short', 'content')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Choice)