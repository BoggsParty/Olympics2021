from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404, HttpResponseRedirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from registration.models import Extended_User
from sports.models import Sport, Sport_Images
from participants.models import Guesses
from registration.forms import Edit_SettingsForm
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
def sport_menu(request):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport = get_list_or_404(Sport, active=True)
    return render(request, 'pages/menu.html',{'sport':sport,})

@login_required(login_url='/accounts/login/')
def sport_detail(request, sport):
    today = datetime.datetime.now()
    now = today.date()
    lock_sports = Sport.objects.exclude(locked=True).filter(lock_date__lte=now)
    lock_sports.update(locked=True)
    sport = get_object_or_404(Sport, slug=sport)
    images = get_list_or_404(Sport_Images, sport=sport)
    guesses = Guesses.objects.filter(user=request.user).filter(sport=sport)
    
    return render(request, 'pages/sport_detail.html',{'sport':sport, 'images':images,'guesses':guesses})

@login_required(login_url='/accounts/login/')
def edit_settings(request):
    #sports_nav = get_list_or_404(Sport)
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings.html', {'form':form,'settings':settings})
 
@login_required(login_url='/accounts/login/') 
def edit_settings_saved(request):
    #sports_nav = get_list_or_404(Sport)
    settings = get_object_or_404(Extended_User, user=request.user)
    if request.method == "POST":
        form = Edit_SettingsForm(request.POST,request.FILES, instance=settings)
        if form.is_valid():
            settings = form.save(commit=False)
            settings.save()
            return redirect('edit-settings-saved')
    else:
        form = Edit_SettingsForm(instance=settings)
    return render(request, 'registration/settings-saved.html', {'form':form,'settings':settings})
    
def log_out (request):
    logout(request)
    return redirect('scores')