from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('', views.home, name = 'website-home'),
    path('blog/', PostListView.as_view(), name = 'website-blog')
]