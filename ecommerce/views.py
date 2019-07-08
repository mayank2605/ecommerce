from django.shortcuts import render
from .forms import ContactForm,Login


def home(request):
    context={
        "title":"hello world!!!",
        "content":"welcome"


    }
  
    return render(request,"home.html", context)

def about(request):
  
    return render(request,"home.html")
def login_page(request):
    form1=Login(request.POST or None)
    if form1.is_valid():
        print(form1.cleaned_data)

    context={
        "loginform":form1

    }    
    
    return render(request,"auth/login.html",context)

def register(request):
    return render(request,"auth/register.html",{})

def contact(request):
    

    contact_form = ContactForm(request.POST or None)
    context = {
        "form":contact_form,
        "brand":"mk"



    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request,"contact/view.html",context)
   