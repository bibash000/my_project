from rest_framework.decorators import api_view
from .serializer import PostSerializer
from rest_framework.response import Response
from .models import Post

@api_view(['GET'])
def post_get(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)