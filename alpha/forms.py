from django import forms


class AboutForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        pass


class AuthForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)


class RegForm(forms.Form):
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50)
