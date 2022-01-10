from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponseRedirect, render_to_response
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from registration.models import Extended_User
from sports.models import Sport, Sport_Images
from participants.models import Guesses
from registration.forms import Edit_SettingsForm, Edit_EmailForm
from django.views.generic.edit import FormView
import datetime


@login_required(login_url='/accounts/login/')
def FAQ(request):
    return render(request, 'pages/faq.html')

@login_required(login_url='/accounts/login/')
def scores(request):
    score = Extended_User.objects.all().order_by('-score')
    return render(request, 'pages/scores.html',{'score':score})
    
@login_required(login_url='/accounts/login/')
def score_calculation(request):  
    today = datetime.datetime.now()
    now = today.date() 
    lock_sports = Sport.objects.exclude(active=False).exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    
    active_sport = Sport.objects.filter(awarded=True, active=True)
    
    for sport in active_sport:
        active_user = User.objects.all()
        winner_gold = sport.gold
        winner_silver = sport.silver
        winner_bronze = sport.bronze
        for user in active_user:
            score = 0
            
            #fully correct
            gold_correct = Guesses.objects.filter(user=user, sport=sport, gold=winner_gold).count()
            silver_correct = Guesses.objects.filter(user=user, sport=sport, silver=winner_silver).count()
            bronze_correct = Guesses.objects.filter(user=user, sport=sport, bronze=winner_bronze).count()
            correct = gold_correct + silver_correct + bronze_correct
            if correct == 1:
                score = 10
            elif correct == 2:
                score = 25
            elif correct == 3:
                score = 50
            else:
                score = 0
            
            #partially correct
            gold_partial_silver = Guesses.objects.filter(user=user, sport=sport, silver=winner_gold).count()
            gold_partial_bronze = Guesses.objects.filter(user=user, sport=sport, bronze=winner_gold).count()
            silver_partial_gold = Guesses.objects.filter(user=user, sport=sport, gold=winner_silver).count()
            silver_partial_bronze = Guesses.objects.filter(user=user, sport=sport, bronze=winner_silver).count()
            bronze_partial_gold = Guesses.objects.filter(user=user, sport=sport, gold=winner_bronze).count()
            bronze_partial_silver = Guesses.objects.filter(user=user, sport=sport, silver=winner_bronze).count()
            partial = gold_partial_silver + gold_partial_bronze + silver_partial_gold + silver_partial_bronze + bronze_partial_gold + bronze_partial_silver
            score = score + (partial*5)
            
            #print (score)
            
            try:
                guess_score = Guesses.objects.get(user=user, sport=sport)
            except: 
                continue
            guess_score.score = score
            #print (guess_score.score)
            guess_score.save()

    user_total = User.objects.all()
    for user in user_total:
        total_score = Guesses.objects.filter(user=user).aggregate(Sum('score'))
        extended_user = Extended_User.objects.get(user=user)
        score_number = total_score['score__sum']
        if score_number != None:
            extended_user.score = score_number
            #print(user, score_number)
            extended_user.save()
        else:
            #print(user,'0')
            continue
    
    return render(request, 'pages/score-calculation.html')
    

@login_required(login_url='/accounts/login/')
def sport_menu(request):
    guess_entered = Guesses.objects.filter(user=request.user)
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(active=False).exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    open_sport = Sport.objects.exclude(active=False).exclude(locked=True).order_by('order')
    closed_sport = Sport.objects.exclude(active=False).exclude(locked=False).order_by('order')
    
    check_guesses = Guesses.objects.filter(user=request.user).count()
    
    if check_guesses == 0:
        no_guesses = True
    else:
        no_guesses = False
    
    return render(request, 'pages/menu.html',{'guess_entered':guess_entered,'open_sport':open_sport,'closed_sport':closed_sport, 'no_guesses':no_guesses})

@login_required(login_url='/accounts/login/')
def sport_detail(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport = get_object_or_404(Sport, slug=sport)
    images = get_list_or_404(Sport_Images, sport=sport)
    guesses = Guesses.objects.filter(user=request.user).filter(sport=sport)
    
    return render(request, 'pages/sport_detail.html',{'sport':sport, 'images':images, 'guesses':guesses})
    
@login_required(login_url='/accounts/login/')
def update_email(request):
    settings = request.user
    if request.method == "POST":
        form = Edit_EmailForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_EmailForm(instance=settings)
    return render(request, 'registration/email_change_form.html', {'form':form,'settings':settings})
    
@login_required(login_url='/accounts/login/')
def edit_settings(request):
    #sports_nav = get_list_or_404(Sport)
    email = request.user
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings.html', {'form':form,'settings':settings,'email':email,})
 
@login_required(login_url='/accounts/login/') 
def edit_settings_saved(request):
    #sports_nav = get_list_or_404(Sport)
    email = request.user
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings-saved.html', {'form':form,'settings':settings,'email':email,})

def log_out (request):
    logout(request)
    return redirect('scores')
    
