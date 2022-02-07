from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, get_list_or_404
from .forms import NewCommentForm, NewResponseForm
from registration.models import Extended_User
from boards.models import Comments, Responses
import datetime

@login_required
def messages_first_page(request):
    extended_user = Extended_User.objects.get(user=request.user)
    q_count = Comments.objects.all().count()
    messages = Comments.objects.all().order_by('-id')[:10]
    responses = Responses.objects.all()
    next_page = 1
    return render (request, 'boards/messages.html',{'messages':messages,'responses':responses,'q_count':q_count,'next_page':next_page, 'extended_user':extended_user,})

@login_required
def messages(request, num):
    extended_user = Extended_User.objects.get(user=request.user)
    num = int(num)
    number_10 = num+10
    next_page = num+1
    previous_page = num-1
    q_count = Comments.objects.all().count()
    final_page = q_count/10#total page count
    if q_count < 20:
        q_start = 10
        messages = Comments.objects.all().order_by('-id')[q_start:]
    else:
        q_start = q_count-(num*10)
        q_end = q_start+10
        messages = Comments.objects.all().order_by('-id')[q_start:q_end]
    responses = Responses.objects.all()
    return render (request, 'boards/messages.html', {'messages':messages,'responses':responses,'next_page':next_page,'previous_page':previous_page,'final_page':final_page,'extended_user':extended_user,})

@login_required   
def new_comment(request):
    extended_user = Extended_User.objects.get(user=request.user)
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm()
    return render(request, 'boards/messages-form.html', {'form':form, 'extended_user':extended_user,})


@login_required  
def new_response(request, pk):
    extended_user = Extended_User.objects.get(user=request.user)
    comment = Comments.objects.get(pk=pk)
    if request.method == "POST":
        form = NewResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.comment = comment 
            response.save()
            return redirect('messages-first-page')
    else:
        form = NewResponseForm()
    return render(request, 'boards/response-messages-form.html', {'form':form, 'extended_user':extended_user,'comment':comment,})


@login_required    
def edit_comment(request, pk):
    extended_user = Extended_User.objects.get(user=request.user)
    comment = get_object_or_404(Comments, pk=pk, user=request.user)
    if request.method == "POST":
        form = NewCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm(instance=comment)
    return render(request, 'boards/messages-form.html', {'form':form, 'extended_user':extended_user,})

@login_required    
def edit_response(request, pk):
    extended_user = Extended_User.objects.get(user=request.user)
    response = get_object_or_404(Responses, pk=pk, user=request.user)
    if request.method == "POST":
        form = NewResponseForm(request.POST, instance=response)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return redirect('messages-first-page')
    else:
        form = NewCommentForm(instance=response)
    return render(request, 'boards/messages-form.html', {'form':form, 'extended_user':extended_user,})
    