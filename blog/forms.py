from django import forms 


class SEND_COMMENT(forms.Form) : 
    name = forms.CharField(max_length= 100 )
    email = forms.EmailField()
    website = forms.CharField(max_length=50)
    Comments = forms.CharField(widget=forms.Textarea) 




class  SEND_CONTACT(forms.Form) : 
    name = forms.CharField(max_length= 100 )
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea) 