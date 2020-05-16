from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Answer, Question, Result


def index(request):
    latest_question_list = Question.objects.order_by('id')[:20]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'survey/index.html', context)
def process(request):
    ei = 0
    ns = 0
    tf = 0
    pj = 0
    for question in Question.objects.all():
        mbti_result = ""
        user_input = request.POST.get('question' + str(question.id), False)
        user_answer = Answer.objects.get(pk=user_input)
        user_answer_type = user_answer.answer_type
        if user_answer_type == 'E':
            ei += 1
        elif user_answer_type == 'I':
            ei -= 1
        elif user_answer_type == 'N':
            ns += 1
        elif user_answer_type == 'S':
            ns -= 1
        elif user_answer_type == 'T':
            tf += 1
        elif user_answer_type == 'F':
            tf -= 1
        elif user_answer_type == 'P':
            pj += 1
        elif user_answer_type == 'J':
            pj -= 1
        
    if ei >= 0:
        mbti_result += "E"
    else:
        mbti_result += "I"
    if ns >=0:
        mbti_result += "N"
    else:
        mbti_result += "S"
    if tf >= 0:
        mbti_result += "T"
    else:
        mbti_result += "F"
    if pj >= 0:
        mbti_result += "P"
    else:
        mbti_result += "J"    
    
    user_result = Result(result_text = mbti_result)
    user_result.save()
    user_result.id
        
    return HttpResponseRedirect(reverse('survey:results', args = [user_result.id]))

def results(request, result_id):
    mbti_result = Result.objects.get(pk=result_id)
    
    return render(request, 'survey/results.html', {'result': mbti_result})
