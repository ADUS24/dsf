from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
# Create your views here.
def profile(request):
    return render(request,'accounts/profile.html')


class userReg(CreateView):
    model=User
    fields=['username','email','password']
    success_url='../login/'
    template_name='accounts/register.html'