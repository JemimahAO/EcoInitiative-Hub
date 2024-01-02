from django import forms
from .models import Event, Initiative, Contact

class AddEventForm(forms.Form):
    title = forms.CharField()
    event_image = forms.FileField()
    event_date = forms.DateField()
    start_time = forms.TimeField()
    end_time = forms.TimeField()
    price = forms.IntegerField()
    location = forms.CharField()
    description = forms.CharField()


choices = [('music', 'Music'), ('art', 'Art'), ('ent', 'Entertainment')]


class AddInitiativeForm(forms.Form):
    class Meta:
        model = Initiative
        fields = ('title', 'category', 'start_date', 'end_date', 'initiative_image', 'description' , 'goals')

        widgets = {
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


# contact us form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'