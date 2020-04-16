from django.contrib import admin

from .models import Question
from .models import Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']})
    ]
    inlines = [AnswerInline]
    list_display = ['question_text']
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text', 'answer_type']




admin.site.register(Question, QuestionAdmin)

admin.site.register(Answer, AnswerAdmin)
