from django.contrib import admin

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('q_id', 'short', 'content')

admin.site.register(Question, QuestionAdmin)