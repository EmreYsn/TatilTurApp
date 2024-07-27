from django import forms
from django.forms import ModelForm
from tatilturapp.models import TatilTur

class SignUpForm(forms.Form):
    username_input = forms.CharField(label="Kullanıcı Adı",max_length=50)

class SignUpModelForm(ModelForm):
    class Meta:
        model = TatilTur
        fields = ["username"]
