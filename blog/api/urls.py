from django.urls import path

'''
from .views import BlogPostRudView, BlogPostAPIView


urlpatterns = [
    path('', BlogPostAPIView.as_view(), name="post-create"),
    path('<str:pk>/', BlogPostRudView.as_view(), name="post-rud"),
]
'''

from rest_framework.routers import DefaultRouter

from blog.api.views import BlogViewSet

router = DefaultRouter()
router.register(r'', BlogViewSet, basename='blog')
urlpatterns = router.urls