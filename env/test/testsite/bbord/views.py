from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb


# Create your views here.


def index(request):
    s = ' Hello \n '
    for x in Bb.objects.order_by('-published'):
        s += x.title + ' ' + x.content
    return HttpResponse(s, content_type='text/plain; charset=UTF-8')

from .models import Rubric
def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics,
               'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)

