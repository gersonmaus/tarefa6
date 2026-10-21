from django import forms
from django.contrib.auth.forms import UserCreationForm
from meu_app.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "quantity"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Nome do produto"}),
            "description": forms.Textarea(attrs={"rows": 4, "placeholder": "Descrição (opcional)"}),
            "price": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "quantity": forms.NumberInput(attrs={"min": "0"}),
        }


class SignUpForm(UserCreationForm):
    pass
