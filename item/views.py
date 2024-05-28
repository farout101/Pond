from django.shortcuts import get_object_or_404, render
from .models import item as ObjItem

# Create your views here.
def detail(request, pk):
    item = get_object_or_404(ObjItem, pk=pk)
    related_items = ObjItem.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
