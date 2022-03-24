from django.urls import path

from main.views import ShowPost, MainView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('post/<int:pk>', ShowPost.as_view(), name='post'),
]