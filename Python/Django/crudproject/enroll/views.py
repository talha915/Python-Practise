from django.shortcuts import render
from .forms import Registration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = Registration()
    else:
        fm = Registration()    
    return render(request, 'enroll/addandshow.html', {'form': fm})