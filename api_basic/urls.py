from django.urls import path, include
from .views import article_list, article_detail
from . import views






urlpatterns = [
    path('list/', article_list),
    path('detail/<int:pk>/', article_detail),
]
