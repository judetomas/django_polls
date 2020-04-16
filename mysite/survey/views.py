from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Answer, Question


def index(request):
    latest_question_list = Question.objects.order_by('id')[:20]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'survey/index.html', context)