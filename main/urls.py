from django.urls import path

from main.views import ShowPost, MainView, UpdatePost, DeletePost, CreatePost, UpdateBlogName

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('post/<int:pk>/', ShowPost.as_view(), name='post'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),
    path('create/', CreatePost.as_view(), name='create'),
    path('update/name/<int:pk>', UpdateBlogName.as_view(), name='update_name'),
]