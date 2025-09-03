from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    color = models.CharField(max_length=20, default="#4299e1")  # e.g. Tailwind colors or hex

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(max_length=300, blank=True)  # short preview text
    content = models.TextField()  # full blog content
    image = models.ImageField(upload_to='images/',blank=True, null=True)  # blog-card-image
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, related_name="posts")
    author_avatar = models.ImageField(upload_to='avatars/',blank=True, null=True)  # profile image
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    cover_photo = models.ImageField(upload_to='profile_pics/', blank=True, default='/static/default_cover.jpg')
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='/static/default_avatar.png')
    skills = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"