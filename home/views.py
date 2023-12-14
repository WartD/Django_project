import math
from django.http import HttpRequest
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import get_object_or_404, render
from . import forms
from django.shortcuts import redirect
from random import randint
from django.shortcuts import render, redirect
from .models import Details
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import uuid
from .utils.diet_plan_generate import days_diet_plan, get_calories

"""
if request.method == "POST":
        try:
            details = Details.objects.get(user=request.user)
        except Details.DoesNotExist:
            details = None

        if details:
            details_form = forms.DetailForm(
                request.POST, user=request.user, instance=details
            )
            if details_form.is_valid():
                details = details_form.save(commit=False)  # type: Details
                details.user = request.user
                details_form.save()
        else:
            details_form = forms.DetailForm(request.POST, user=request.user)

            if details_form.is_valid():
                details = details_form.save(commit=False)  # type: Details
                if request.user.is_authenticated:
                    details.user = request.user
                    details_form.save()
                else:
                    details.user = None
                    details_form.save()
                    return redirect("register")

        return redirect("index")
"""


# Создайте здесь свои представления.
def index(request: HttpRequest):
    detail_form = forms.DetailForm(user=request.user)
    context = {"form": detail_form, "message": "0"}

    if request.method == "POST":
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        age = request.POST.get("age")
        activity = request.POST.get("activity")
        number_of_days = request.POST.get("number_of_days")

        if not request.user.is_authenticated:
            request.session["details"] = dict()
            request.session["details"]["name"] = name
            request.session["details"]["gender"] = gender
            request.session["details"]["weight"] = weight
            request.session["details"]["height"] = height
            request.session["details"]["age"] = age
            request.session["details"]["activity"] = activity
            request.session["details"]["number_of_days"] = number_of_days
            request.session.modified = True
        else:
            try:
                details = Details.objects.get(user=request.user)
            except Details.DoesNotExist:
                details = None

            if details:
                details_form = forms.DetailForm(
                    request.POST, user=request.user, instance=details
                )
                if details_form.is_valid():
                    details = details_form.save(commit=False)
                    details.user = request.user
                    details_form.save()

        return redirect("index")

    else:
        # Бизнес-логика здесь
        if request.user.is_authenticated:
            try:
                details = Details.objects.get(user=request.user)
            except Details.DoesNotExist:
                details = None
        else:
            if "details" in request.session:
                details = request.session.get("details", None)
            else:
                details = None
        if details:
            if isinstance(details, dict):
                name = details["name"]
                gender = details["gender"]
                weight = details["weight"]
                height = details["height"]
                age = details["age"]
                activity = details["activity"]
            else:
                name = details.name
                gender = details.gender
                weight = details.weight
                height = details.height
                age = details.age
                activity = details.activity

            context["message"] = "1"
            context["name"] = name
            context["gender"] = gender
            context["height"] = height
            context["weight"] = weight
            w = float(weight) if weight else 0
            h = float(height) if height else 0
            age = int(age) if age else 0
            act = activity
            gender = gender
            context["cal"] = get_calories(
                gender=gender,
                weight=w,
                height=h,
                age=age,
                activity=act,
            )

            diet = get_diet(details, request)
            context["diets"] = diet
            context["message"] = "1"
        else:
            context["message"] = "0"

        return render(request, "index.html", context=context)


def get_diet(details, request) -> dict | None:
    if isinstance(details, dict):
        gender = details["gender"]
        weight = details["weight"]
        height = details["height"]
        age = details["age"]
        activity = details["activity"]
        number_of_days = details["number_of_days"]
    else:
        gender = details.gender
        weight = details.weight
        height = details.height
        age = details.age
        activity = details.activity
        number_of_days = details.number_of_days

        return days_diet_plan(
            gender=gender,
            weight=weight,
            height=height,
            age=age,
            activity=activity,
            number_of_days=number_of_days,
        )


def registerPage(request):
    form = RegisterForm()

    if request.method == "POST":
        # заполняем объект данными формы, если она была отправлена
        form = RegisterForm(request.POST)

        if form.is_valid():
            # если форма валидна - создаем нового пользователя
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            if "details" in request.session:
                detail = Details()
                detail.user = user
                detail.name = request.session["details"]["name"]
                detail.gender = request.session["details"]["gender"]
                detail.weight = request.session["details"]["weight"]
                detail.height = request.session["details"]["height"]
                detail.age = request.session["details"]["age"]
                detail.activity = request.session["details"]["activity"]
                detail.number_of_days = request.session["details"]["number_of_days"]
                detail.save()
                del request.session["details"]
            else:
                # Пустой объект деталей
                detail = Details()
                detail.user = user
                detail.save()

            return redirect("login")
    # ренедерим шаблон и передаем объект формы
    return render(request, "registration/registration.html", {"form": form})


def me(request):
    if not request.user.is_authenticated:
        return redirect("login")

    details, _ = Details.objects.get_or_create(user=request.user)
    form_detail = forms.DetailForm(instance=details, user=request.user)
    form_photo = forms.UserPhotoForm()

    if request.method == "POST":
        if "user_photo" in request.FILES:
            form_photo = forms.UserPhotoForm(request.POST, request.FILES)
            if form_photo.is_valid():
                details.user_photo = form_photo.cleaned_data["user_photo"]
                details.save()

        details_form = forms.DetailForm(
            request.POST, instance=details, user=request.user
        )
        if details_form.is_valid():
            details_form.save()

        return redirect("me")
    context = {
        "form": form_detail,
        "form_photo": form_photo,
        "user_photo": details.user_photo,
    }
    return render(request, "me.html", context=context)


def contact(request):
    return render(request, "contact.html")
