from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
        
        self.fields["name"].widget.attrs.update({"placeholder": "Enter your name..."})
        self.fields["email"].widget.attrs.update({"placeholder": "Enter your email..."})
        self.fields["phone"].widget.attrs.update({"placeholder": "Enter your phone number..."})
        self.fields["message"].widget.attrs.update({"placeholder": "Enter your message here..."})