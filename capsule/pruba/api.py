from rest_framework.decorators import api_view
from .serializer import PostSerializer, CommentSerializer, CategorySerializer, ProfileSerializer
from rest_framework.response import Response
from .models import Post,Comment,Category,Profile
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def post_get(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = PageNumberPagination()
    paginated_posts = paginator.paginate_queryset(posts, request)
    serializer = PostSerializer(paginated_posts, many=True)
    return paginator.get_paginated_response(serializer.data)

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

@api_view(['POST'])
def profiles_api(request):
    if request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({
                'message':'cant post data'
            }, status=400)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def post_add(request):
    if request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({
                'message':"Can't post data"
            }, status=400)

@api_view(['POST'])
def comment_add(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({
                'message':"Can't post data"
            }, status=400)


@api_view(['POST'])
def categories_add(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({
                'message':"Can't post data",
                'errors':serializer.errors
            },
            status=400
        )

