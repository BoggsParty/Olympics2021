from django.forms import ModelForm
from django import forms
from .models import Comments, Responses

class NewCommentForm(ModelForm):
    
    class Meta:
        model = Comments
        fields = ('message',)
        
class NewResponseForm(ModelForm):
    
    class Meta:
        model = Responses
        fields = ('message',)
    