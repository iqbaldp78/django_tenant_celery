from rest_framework import routers
from .views import  ConcurrentCreateViewSet,ConcurrentDetailCreateViewSet
from django.conf.urls import url,include

router = routers.SimpleRouter()

#define concurrent
router.register(r'MasterConcurrents',ConcurrentCreateViewSet)
router.register(r'MasterDetailConcurrents',ConcurrentDetailCreateViewSet)


urlpatterns = [url(r'^',include(router.urls))]


