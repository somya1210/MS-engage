from django import forms

from .models import Query,Comment

# forms for query
class QueryForm(forms.ModelForm):

    class Meta:
        model = Query
        fields = ('title', 'content','author','slug')
        widgets = { # change attribute of the original class to
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'auth','type':'hidden'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

# form for comment
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','body')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','value':'','id':'user'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }