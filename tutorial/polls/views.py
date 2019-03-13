# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.

from django.http import HttpResponse
#from django.template import loader - deprecated because index can use render instead


#SHORTCUTS
#render: load template + fill a context + return HttpResponse
#get_object_or_404: get() + raise Http404 if the object doesn't exist
## see also get_list_or_404(): filter + raise Http404 if list is empty
from django.shortcuts import get_object_or404, render

from .models import Question

# index based on loader
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

#index based on render
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

#detail with get + raise Http404
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

#detail with get_object_or_404() (and render)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
