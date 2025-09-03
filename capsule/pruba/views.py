from django.shortcuts import render,get_object_or_404, redirect
from .models import Post,Category,Comment,Profile
from .forms import CommentForm,ProfileForm,UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def home(request):
    x=Post.objects.all()
    paginator = Paginator(x, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def logged(request):
    return render(request, 'logged.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'form': form})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        password0 = request.POST.get("password0")
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        if password != password0:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return render(request,'login.html')

@login_required
def add_post(request):
    categories = Category.objects.all()  

    if request.method == 'POST':
        title = request.POST.get('title')
        excerpt = request.POST.get('excerpt')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        author_name = request.POST.get('author')
        author_avatar = request.FILES.get('author_avatar')

        category = Category.objects.get(id=category_id) if category_id else None

        post = Post.objects.create(
            title=title,
            excerpt=excerpt,
            content=content,
            image=image,
            category=category,
            author=request.user,
            author_avatar=author_avatar
        )
        post.save()
        return redirect('home') 

    return render(request, 'add_post.html', {'categories': categories})
@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    categories = Category.objects.all()

    if request.method == "POST":
        post.title = request.POST.get("title")
        post.excerpt = request.POST.get("excerpt")
        post.content = request.POST.get("content")
        category_id = request.POST.get("category")
        post.category = Category.objects.get(id=category_id) if category_id else None
        if request.FILES.get("image"):
            post.image = request.FILES["image"]
        post.save()
        return redirect("home")
    return render(request, "update.html", {"post": post, "categories": categories})

from django import template
register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

 
    if request.user != post.author:
        return redirect("home")

    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(request, "delete_post.html", {"post": post})

def profile_view(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        avatar_url = profile.avatar.url if profile.avatar else '/static/default_avatar.png'
        cover_url = profile.cover_photo.url if profile.cover_photo else '/static/default_cover.jpg'
        
     
        skills_list = [s.strip() for s in profile.skills.split(',')] if profile.skills else []
        if profile.skills:
            skills_list = [skill.strip() for skill in profile.skills.split(',')]

        return render(request, "profile.html", {
            "profile": profile,
            "skills_list": skills_list,  
            "avatar_url": avatar_url,
            "cover_url": cover_url
        })
    return redirect("login")

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        profile.bio = request.POST.get('bio')
        profile.skills = request.POST.get('skills')
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']
        if 'cover_photo' in request.FILES:
            profile.cover_photo = request.FILES['cover_photo']
        profile.save()

        return redirect('profile')

    context = {
        'user': request.user,
        'profile': profile
    }
    return render(request, 'edit_profile.html', context)

for user in User.objects.all():
    if not hasattr(user, 'profile'):
        Profile.objects.create(user=user)