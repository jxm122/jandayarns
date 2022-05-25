from django.shortcuts import render

# Create your views here.
def bralettes(request):
   return render(request,'gallery/bralettes.html') 

def bandanas(request):
   return render(request,'gallery/bandanas.html') 

def bags(request):
   return render(request,'gallery/bags.html')

def ties(request):
   return render(request,'gallery/ties.html')