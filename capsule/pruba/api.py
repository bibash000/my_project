from rest_framework.decorators import api_view
from .serializer import PostSerializer, CommentSerializer, CategorySerializer, ProfileSerializer
from rest_framework.response import Response
from .models import Post,Comment,Category,Profile

@api_view(['GET'])
def post_get(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comments_api(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def categories_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def profiles_api(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)
