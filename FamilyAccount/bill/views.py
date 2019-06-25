from django.shortcuts import render,HttpResponse,redirect
from django.views import View

# Create your views here.

class Home(View):
    def get(self,request):
        print(request.method)
        # return HttpResponse('home')
        return render(request,'bill/home.html')