from django import forms



class ContactForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    category = forms.ChoiceField(choices=[('Boy','Boy'),('Girl','Girl')])
    about = forms.CharField(widget=forms.Textarea)
