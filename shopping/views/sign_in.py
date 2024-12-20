from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) # authentication only
        login(request, user) # successful auth is now added to session
        return redirect('cartitem-list') # its the model name that you are selecting, its also same as the db, plus use '-list' for Django Rest Framework's (DRF) alias.



    return render(request, template_name='SignIn.html')