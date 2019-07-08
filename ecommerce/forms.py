from django import forms


class ContactForm(forms.Form):

    fullname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"your full name"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"your email"}))
    contents=forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":""}))


    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email has to be gmail.com")
        return email        


class Login(forms.Form): 
    username=forms.CharField()
    password=forms.CharField()       