from django.shortcuts import render

from page.models import Contact

# Create your views here.
def home(request):
   return render(request,'page/home.html') 

def about(request):
   return render(request,'page/about.html') 

def contactus (request):
    if request.method == 'POST':
        # Get data from the form
        v_name = request.POST.get('username')
        v_email = request.POST.get('usermail')
        v_message = request.POST.get('message')

        # Send the data to DB (models)
        v_contact = Contact(name=v_name, email=v_email, massage=v_message)
        v_contact.save()

        return render(request, 'page/thank.html')
    else:
        return render(request, 'page/contact.html')
