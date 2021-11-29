from django import forms
from .models import *

class CriminalForm(forms.ModelForm):
    # crime=forms.ModelChoiceField(queryset=crime.objects.all()))
    # documents=forms.ModelChoiceField()
    class Meta:
        model = criminal
        fields = "__all__"
        # labels = {
        #     'fname': 'First Name',
        #     'lname': 'Last Name',
        #     'sex': 'Gender'
        # }
        # widgets = {
        #     'fname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'lname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'dob': forms.DateInput(attrs={'class': 'form-control'}),
        #     'email': forms.DateInput(attrs={'class': 'form-control'}),
        #     'martial_status': forms.DateInput(attrs={'class': 'form-control'}),
        #     'contact_no': forms.DateInput(attrs={'class': 'form-control'}),
        #     'height': forms.DateInput(attrs={'class': 'form-control'}),
        #     'language': forms.DateInput(attrs={'class': 'form-control'}),
        #     'status': forms.DateInput(attrs={'class': 'form-control'}),
        #     'identification': forms.DateInput(attrs={'class': 'form-control'}),
        #     'residence': forms.DateInput(attrs={'class': 'form-control'}),
        #     'sex': forms.DateInput(attrs={'class': 'form-control'}),


        # }

class CrimeForm(forms.ModelForm):
    class Meta:
        model = crime
        fields = "__all__"

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = "__all__"

