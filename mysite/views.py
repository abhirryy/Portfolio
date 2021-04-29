from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home (request):
    work = Work.objects.all()
    
    form = Contactform(request.POST or None)
    if request.method ==  "POST":
        if form.is_valid():
            form.save()

    context ={  'work':work, 'form':form }
    return render(request, 'mysite/index.html',context)



            