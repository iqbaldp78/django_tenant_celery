from rest_framework import routers
from .views import concurrentListViewSet\
    # ,concurrentListViewSet \
    # ,ConcurrentDetailCreateViewSet
from django.conf.urls import url,include

router = routers.SimpleRouter()
router.register(r'Concurrents',concurrentListViewSet)


urlpatterns = [url(r'^',include(router.urls))]


