from django.shortcuts import redirect, render
from .forms import EntryForm
from .models import Entry
from django.contrib.auth.decorators import login_required
from .decorators import *


def index(request):
    entries = Entry.objects.all().order_by('-date_posted')

    context = {'entries':entries}

    return render(request, 'entries/index.html', context)



@admin_only
@login_required(login_url='home')
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    
    form = EntryForm()

    context = {'form':form}

    return render(request, 'entries/add.html', context)


