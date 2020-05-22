from django.shortcuts import render, redirect, reverse
from .models import Item
from .forms import inputItem
from .models import Item

# Create your views here.
def add_item(request):
    return render(request, 'additem.html')

def input_item(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # category = request.POST.get('category')
        # time = request.POST.get('time')
        # author = request.user.username
        # item = Item(name=name, category=category, time=time, author=author)
        # item.save()

        item = inputItem(request.POST)
        if item.is_valid():
            instance = item.save(commit=False)
            instance.author = request.user.username
            instance.save()

        return redirect(reverse('profile'))
     