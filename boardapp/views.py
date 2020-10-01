from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

# Create your views here.

def signupfunc(request):
    #ターミナルでQuerySetの確認。
    #user2 = User.objects.all()
    user2 = User.objects.get(username='yoshi')
    print(user2)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #エラーが出そうな時に使う。
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error':'このユーザーは、登録されています'})
        except:
            user = User.objects.create_user(username, '', password)
            #print(request.POST) postをターミナルで確認できる
            return render(request, 'signup.html', {'some':100})
    #renderメソッド
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        #なくない。is not None
        if user is not None:
            login(request, user)
            #Redirect to a success page.
            return redirect('signup')
        else:
            # Rerutn an 'invalid login' error message.
            return redirect('login')
    return render(request, 'login.html')