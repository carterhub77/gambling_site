from urllib import response
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse

from .cardpack import PackOfCards
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

def newpack(request):    
    newDeck = PackOfCards()
    request.session['currentDeck'] = newDeck
    request.session['currentCard'] = newDeck.cards[0]
    context = {'currentDeck': len(newDeck.cards), 'currentCard':newDeck.cards[0]}
    return render(request,"website\pack.html",context)

def newcard(request):    
    currentdeck = request.session['currentDeck'] 
    del currentdeck.cards[0]
    request.session['currentDeck'] = currentdeck

    context = {'currentDeck': len(currentdeck.cards), 'currentCard':currentdeck.cards[0]}
    return render(request,"website\pack.html",context)

def shuffle(request):    
    currentdeck = request.session['currentDeck'] 
    del currentdeck.cards[0]
    request.session['currentDeck'] = currentdeck

    context = {'currentDeck': len(currentdeck.cards), 'currentCard':currentdeck.cards[0]}
    return render(request,"website\pack.html",context)    