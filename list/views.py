from django.shortcuts import render, redirect
from .models import Item
from .forms import AddItemForm
from .filters import DateFilter


# Create your views here.

def home(request):
    date_filter = DateFilter(request.GET, queryset=Item.objects.all())
    pending_item_list = list(DateFilter(request.GET, queryset=Item.objects.all()).qs.filter(item_status="PENDING"))
    unavailable_item_list = list(DateFilter(request.GET, queryset=Item.objects.all()).qs.filter(item_status="NOT AVAILABLE"))
    bought_item_list = list(DateFilter(request.GET, queryset=Item.objects.all()).qs.filter(item_status="BOUGHT"))

    #pending_item_list = list(Item.objects.filter(item_status="PENDING"))
    #unavailable_item_list = list(Item.objects.filter(item_status="NOT AVAILABLE"))
    #bought_item_list = list(Item.objects.filter(item_status="BOUGHT"))
    return render(request, 'list/index.html',
                  {'pending_items': pending_item_list, 'unavailable_items': unavailable_item_list,
                   'bought_items': bought_item_list, 'date_filter': date_filter,})


def add(request):
    form = AddItemForm()
    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'list/add.html', {'form': form})


def update(request, pk):
    item = Item.objects.get(id=pk)
    form = AddItemForm(instance=item)
    if request.method == "POST":
        form = AddItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'list/update.html', {'form': form})


def delete(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, 'list/delete.html', {'item': item})
