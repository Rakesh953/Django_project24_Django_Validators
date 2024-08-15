from django import forms
from app.models import *

class TopicForms(forms.Form):
    topicname=forms.CharField(max_length=100)


def check_for_a(subvalue):
    # if subvalue[0].lower() == 'a':
    # if len(subvalue)<5 and subvalue[0].lower() == 'a':
    if len(subvalue)<5 :
        raise forms.ValidationError('enter value is a')


class WebpageForm(forms.Form):
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100, validators=[check_for_a])
    url=forms.URLField()

class TopicModelForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'





class WebpageModelForm(forms.ModelForm):
    class Meta:
        model=Webpage
        #fields='__all__'
        #fields=['topic_name','name']
        exclude=['url']