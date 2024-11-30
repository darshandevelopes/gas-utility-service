from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']
        widgets = {
            'request_type': forms.Select(attrs={
                'class': 'block border border-gray-300 rounded-md p-2'
            }),
            'description': forms.Textarea(attrs={
                'class': 'block w-full border border-gray-300 rounded-md p-2',
                'rows': 4
            }),
            'attachment': forms.ClearableFileInput(attrs={
                'class': 'block w-full text-gray-700'
            }),
        }
