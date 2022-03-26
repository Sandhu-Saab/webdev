from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView
from .views import Articledetail, GenericAPIView, ArticleViewSet
from . import views
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('list/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('article_api/', ArticleAPIView.as_view()),
    path('generic_api/<int:id>', GenericAPIView.as_view()),
    path('api_detail/<int:id>/', Articledetail.as_view()),
]
