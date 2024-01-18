from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse

from .models import Question, Choice

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app1/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
#これでも行けるよ
#def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'app1/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #これでも行けるよ
    # question = get_object_or_404(Question. pk=question_id)
    return render(request, 'app1/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app1/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
    #質問回答フォームを再表示
        return render(request, 'app1/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice." ,
    })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #POSTデータが正しく処理されたら、いつもHttpResponseRedirectを返す。
        #これは、ユーザーがブラウザの「戻るボタン」を押してしまった時にもう一度POSTデータが送信されるのを防ぐため。
    return HttpResponseRedirect(reverse('app1:results', args=
(question_id,)))