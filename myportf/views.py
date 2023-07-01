from django.shortcuts import render 
from myportf.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'index.html')

def contact(reqeust):
    if reqeust.method == "POST":
        name = reqeust.POST.get('name')
        email=reqeust.POST.get('email')
        message=reqeust.POST.get('message')
        data= Contact(name=name,email=email,message=message)
        data.save()
            
    return render(reqeust,'contact.html')