from django import forms
from .models import User, Deal, Review


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'description', 'customer', 'performer']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating', 'reviewer']
