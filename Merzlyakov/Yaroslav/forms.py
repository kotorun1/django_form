from django import forms

class AdressForm(forms.Form):
    name =  forms.CharField()
    surname =  forms.CharField()
    side =  forms.CharField()
    region =  forms.CharField()
    city =  forms.CharField()
    street =  forms.CharField()
    house =  forms.IntegerField()