from django.shortcuts import render

from item.models import category, item

# Create your views here.
def index(request):
    items = item.objects.filter(is_sold=False)[0:6]
    categories = category.objects.all()
    return render(request, 'core/index.html', {
        'items': items,
        'categories': categories,
    })


def contact(request):
    return render(request, 'core/contact.html')