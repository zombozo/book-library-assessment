from django.urls import include, path

from library.API.views import BookViewSet
from . import views
from rest_framework import routers

app_name="library"

router = routers.DefaultRouter()
router.register(r'api/books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
]