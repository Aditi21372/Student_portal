from django import forms

class RollNumberForm(forms.Form):
    roll_number = forms.CharField(label='Enter Student Roll Number', max_length=100)
