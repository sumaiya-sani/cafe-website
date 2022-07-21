
from dataclasses import fields
from django import forms
from.models import Review, cafe
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class ReviewsForm(forms.ModelForm):
    class Meta:
      
        model=Review
        fields=["rating","content",]
        lable={
            "rating": "rating",
            "content": "content",
           
        }

        Widget={
        
        "content":forms.Textarea(),
        "rating":forms.MultipleChoiceField()
        
         }  
 

class AddcafeForm(forms.ModelForm):
    class Meta:

        model=cafe 
        fields= ["name","disc","picture","recent_picture","city","working_hours","signture","slug"]

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        email=forms.EmailField(required=True)
        fields = ["username", "email", "password1", "password2"]
  

class EditForm(UserChangeForm):
    email=forms.EmailField()
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    last_login=forms.CharField(max_length=255)
    password=forms.CharField(max_length=100)

    class Mata:
        models=User
        fields=['username','first_name','last_name','last_login','password',]


  
class LoginForm(forms.ModelForm):
    class Meta:
       model=User
       fields=['username','password']    

	



