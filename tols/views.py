from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from tols.models import Question
from django.utils import timezone
from django.http import Http404

def index(request):
    l=Question.order_by('-pub_date')[:5]

    context = {'latest_question_list': l}
    return render(request, 'tols/index.html', context)
def creat(request):
    for i in range(10):
        q=Question()
        q.question_text(f'whats up{i}')
        q.pub_date=timezone.now()
        q.save()
        return HttpResponse('sucess')
def detail(request,question_id):
    # return HttpResponse(f"you are looking {question_id}")
    # try:
        # question = Question.objects.get(pk=question_id)
    question =get_object_or_404(Question,pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
def mypow(request,a,b):
    return HttpResponse("you are looking at %s."% a**b)
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
def factorial(request,n):
    return HttpResponse(f"{n}!={fact(n)}")
def result(request,question_id):
    response=f"you are looking at question"
    return HttpResponse(response,question_id)
def vate(request,question_id):
    return HttpResponse(f"you are looking {question_id}")

# Create your views here.
