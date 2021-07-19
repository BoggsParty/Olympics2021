from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from .forms import GuessForm
from sports.models import Sport, Sport_Images
from registration.models import Extended_User
from participants.models import Guesses
import datetime

@login_required(login_url='/accounts/login/')
#pop out window that closes on save
def guess(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport_query = Sport.objects.get(slug=sport)
    try:
        instance = Guesses.objects.filter(sport=sport_query).get(user=request.user)
    except:
        instance = None

    if instance:
        if request.method == "POST":
            form = GuessForm(request.POST, sport=sport, instance=instance)
            if form.is_valid():
                guess = form.save(commit=False)
                guess.user = request.user
                guess.sport = sport_query
                guess.save()
                form.save_m2m()
                return redirect ("guess_saved")

        else:
            form = GuessForm(sport=sport, instance=instance)
            
    else:
        if request.method == "POST":
            form = GuessForm(request.POST, sport=sport)
            if form.is_valid():
                guess = form.save(commit=False)
                guess.user = request.user
                guess.sport = sport_query
                guess.save()
                form.save_m2m()
                return redirect ("guess_saved")

        else:
            form = GuessForm(sport=sport)
    
    return render(request, 'participants/guess.html',{'form':form,'sport_query':sport_query,})
    
@login_required(login_url='/accounts/login/')
def guess_saved(request):
    return render(request, 'pages/guess_saved.html')    
    
@login_required(login_url='/accounts/login/')    
def all_guess_one_user(request):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    guesses = Guesses.objects.filter(user=request.user)
    sport = Sport.objects.exclude(active=False).order_by('order')
    return render (request, 'participants/guess-all.html', {'guesses':guesses, 'sport':sport})

@login_required(login_url='/accounts/login/')   
def all_guess_all_users(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport = get_object_or_404(Sport, slug=sport)
    guesses = Guesses.objects.filter(sport=sport)
    return render (request, 'participants/guess-all-per-sport.html', {'guesses':guesses, 'sport':sport,})