from django import forms
from .models import User

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["nickname"]

#     def signup(self,request,user):
#         user.nickname = self.cleaned_data["nickname"]
#         user.save()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_pic",
            "intro",
        ]
        widgets = {
            "intro": forms.Textarea,
        }