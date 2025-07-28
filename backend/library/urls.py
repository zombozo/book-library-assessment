from django.urls import include, path

from library.API.views import BookViewSet, CategoryViewSet
from . import views
from rest_framework import routers

app_name="library"

router = routers.DefaultRouter()
router.register(r'api/books', BookViewSet)
#router.register(r'api/category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]