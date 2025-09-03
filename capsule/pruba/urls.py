from .views import *
from .api import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signed_in', logged, name='logged'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('add_post/',add_post, name='add_post'),
    path('update/<int:post_id>/',update_post, name='update_post'),
    path('delete/<int:post_id>/',delete_post, name='delete_post'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]


urlpatterns=[
    path('api/posts/', post_get, name='post_get'),
    path('api/comments/', comments_api, name='comments_api'),
    path('api/categories/', categories_api, name='categories_api'),
    path('api/profiles/', profiles_api, name='profiles_api'),
]