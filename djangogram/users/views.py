from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from djangogram.users.forms import SignUpForm       

def main(request):
    if request.method == 'GET':
        return render(request, 'users/main.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 리다이렉트로 로그인받으면 돌려보내줌
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))
        else:
            # 로그인 실패시 메인화면 다시 띄움
            return render(request, 'users/main.html')
        
def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
        
        return render(request, 'users/signup.html', {'form': form})
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # 리다이렉트로 로그인받으면 돌려보내줌
                login(request, user)
                return HttpResponseRedirect(reverse('posts:index'))
            
        return render(request, 'users/main.html')