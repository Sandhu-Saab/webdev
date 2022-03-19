from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, Articledetail
from . import views






urlpatterns = [
    path('list/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('api/', ArticleAPIView.as_view()),
    path('api_detail/<int:id>/', Articledetail.as_view()),
]
