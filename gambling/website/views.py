from urllib import response
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from .models import Game

def index(request):
    latestGames = Game.objects.order_by('-pk')[:5]
    context = {'latestGames':latestGames}
    return render(request,"website\games_index.html",context)

def login(request):    
    return render(request,"website\login.html")

def loginprocess(request):    
    if not 'username' in request.POST:
        return redirect('/login')

    username = request.POST['username']
    
    resp = index(request)
    resp.set_cookie('username', username)

    return resp

def newgame(request):

    if not 'username' in request.COOKIES:
        return redirect('/login')

    latestGames = Game()
    latestGames.status='Open'
    latestGames.save()

    return redirect('/')