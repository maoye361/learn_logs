from django import forms
from .models import Topic,Entry,Addfile
class TopicFrom(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        lables = {'text': ''}
class EntryFrom(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        lables = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
class AddfileFrom(forms.ModelForm):
    class Meta:
        model = Addfile
        fields = ['upload']
        lables = {'upload': ''}