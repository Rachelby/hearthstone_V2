from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render


from .models import Card


def index(request):
    cards_list = Card.objects.order_by('name')[:5]
    template = loader.get_template('cards/index.html')
    context = {
        'cards_list': cards_list,
    }
    return HttpResponse(template.render(context, request))

# def index(request):
#     return HttpResponse("Hello, world. You're at the cards index.")

def list(request):
    return HttpResponse("Hello, world. You're at the cards list.")

def detail(request, card_id):
    try:
        card = Card.objects.get(pk=card_id)
    except Card.DoesNotExist:
        raise Http404("Card does not exist")
    return render(request, 'cards/details.html', {'card': card})

def edit(request, card_id):
    return HttpResponse("You're editing card %s." % card_id)