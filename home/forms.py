# forms.py

from django import forms
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, validate_email
from django.forms import ModelForm, PasswordInput

from .models import Details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DetailForm(forms.ModelForm):
    age = forms.IntegerField(
        label="Возраст",
        min_value=0,
        max_value=110,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Ваш возраст"},
        ),
        required=True,
    )

    weight = forms.IntegerField(
        label="Вес",
        min_value=0,
        max_value=200,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Ваш вес (в кг)"}
        ),
        required=True,
    )

    height = forms.IntegerField(
        label="Рост",
        min_value=0,
        max_value=250,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Ваш рост (в см)"}
        ),
        required=True,
    )

    number_of_days = forms.ChoiceField(
        label="Количество дней",
        choices=Details.number_of_days_choices,
        widget=forms.Select(attrs={"class": "form-control"}),
        required=True,
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(DetailForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            try:
                details = Details.objects.get(user=user)
                self.initial["name"] = details.name
                self.initial["gender"] = details.gender
                self.initial["age"] = details.age
                self.initial["weight"] = details.weight
                self.initial["height"] = details.height
                self.initial["activity"] = details.activity
                self.initial["number_of_days"] = details.number_of_days
            except Details.DoesNotExist:
                pass

    class Meta:
        model = Details
        fields = ["name", "gender", "age", "weight", "height", "activity", "number_of_days"]
        labels = {
            "name": "Полное имя",
            "gender": "Пол",
            "age": "Возраст",
            "weight": "Вес",
            "height": "Рост",
            "activity": "Физическая активность",
            "number_of_days": "Количество дней",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Полное имя"}
            ),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "height": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Ваш рост (в см)"}
            ),
            "activity": forms.Select(attrs={"class": "form-control"}),
        }


class RegisterForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]

    username = forms.CharField(
        min_length=3,
        max_length=15,
        required=True,
        label="Логин",
        validators=[
            RegexValidator(
                regex="^[a-zA-Z0-9]*$",
                message="Может содержать только латинские буквы и цифры",
                code="invalid_username",
            ),
        ],
        widget=forms.TextInput(attrs={"placeholder": "Логин"}),
    )

    email = forms.CharField(
        min_length=3,
        required=True,
        label="Почта",
        widget=forms.TextInput(attrs={"placeholder": "Почта"}),
    )

    password = forms.CharField(
        widget=PasswordInput(attrs={"placeholder": "Пароль"}),
        required=True,
        label="Пароль",
        min_length=0,
    )
    password_confirm = forms.CharField(
        widget=PasswordInput(attrs={"placeholder": "Повторите пароль"}),
        required=True,
        label="Повторите пароль",
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        # валидация паролей
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError(
                {"password_confirm": "Пароли не совпадают", "password": ""}
            )
        # валидация никнейма
        username = self.cleaned_data.get("username")

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError({"username": "Такой логин уже занят"})

        # валидация email
        try:
            validate_email(self.cleaned_data.get("email"))
        except ValidationError as e:
            raise forms.ValidationError({"email": "Почта не является валидной"})

        return cleaned_data


class UserPhotoForm(forms.Form):
    user_photo = forms.ImageField(
        required=False,
        label="Фото",
        widget=forms.FileInput(),
    )
