from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username, '', password)
        #print(request.POST) postをターミナルで確認できる
        return render(request, 'signup.html', {'some':100})
    #renderメソッド
    return render(request, 'signup.html', {'some':100})