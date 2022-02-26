from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import learning ,learningcatagory,LearningSeries
# from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewuserForm

# Create your views here.
def single_slug(request, single_slug):
    catagories = [c.catagory_slug for c in learningcatagory.objects.all()]
    if single_slug in catagories:
        matching_series = LearningSeries.objects.filter(learning_category__catagory_slug=single_slug)
        series_urls={}

        for m in matching_series.all():
            part_one = learning.objects.filter(learning_series__learning_series=m.learning_series).earliest("learning_published")
            series_urls[m]=part_one.learning_slug
        return render(request,
                      "main/catagory.html",
                      {"part_ones":series_urls})

    learningq = [t.learning_slug for t in learning.objects.all()]
    if single_slug in learningq:
        this_learning = learning.objects.get(learning_slug= single_slug)
        learning_from_series = learning.objects.filter(learning_series__learning_series=this_learning.learning_series).order_by("learning_published")
        this_learning_idx = list(learning_from_series).index(this_learning)

        return render(request,
                      "main/learning.html",
                      {"learning" : this_learning,
                       "sidebar": learning_from_series,
                       "this_learning_idx":this_learning_idx})

    return HttpResponse(f"{single_slug} does not response to anything !!!")


def homepage(request):
    return render(request = request,
                  template_name="main/catagories.html",
                  context={"catagories": learningcatagory.objects.all})

def register(request):
    if request.method == "POST":
        form = NewuserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request,user)
            messages.info(request, f"You are now logged in as : {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request,f"{msg}:{form.error_messages[msg]}")

    form = NewuserForm
    return render(request,
                  "main/register.html",
                  context={"form" : form})

# def register(request):
#     # if request.method == "POST":
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         user = form.save()
#     #         username = form.cleaned_data.get('username')
#     #         login(request, user)
#     #         return redirect("main:homepage")
#     #
#     #     else:
#     #         for msg in form.error_messages:
#     #             print(form.error_messages[msg])
#     #
#     #         return render(request = request,
#     #                       template_name = "main/register.html",
#     #                       context={"form":form})
#     #
#     form = UserCreationForm
#     return render(request = request,
#                   template_name = "main/register.html",
#                   context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request , "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username ,password=password)
            if user is not None:
                login(request,user)
                messages.info   (request, f"You are now logged in as : {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})
