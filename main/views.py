# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate, login , logout
# from .froms import SignupForm, LoginForm, ArticleForm
# from .models import Article

# # Create your views here.
# # Home page
# def index(request):
#     return render(request, 'index.html')

# # signup page
# def user_signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

# # login page
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)    
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

# def blog(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('blog')
#     else:
#         form = ArticleForm()
#     articles = Article.objects.all().order_by('-pub_date')
#     return render(request, 'blog.html', {'form': form, 'articles': articles})

# # logout page
# def user_logout(request):
#     logout(request)
#     return redirect('login')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .froms import SignupForm, LoginForm, ArticleForm
from .models import Article

# Home page
def index(request):
    return render(request, 'index.html')

# Signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('blog')  # Redirect to blog page after successful login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Blog page
def blog(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')  # Redirect to same page after adding new article
    else:
        form = ArticleForm()
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog.html', {'form': form, 'articles': articles})

# Logout page
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
