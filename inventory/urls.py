from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from inventory.views import ItemViewSet, ContainerViewSet, ItemTagViewSet, InfoView

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'containers', ContainerViewSet, basename='container')
router.register(r'item-tags', ItemTagViewSet)


urlpatterns = [
    url(r'^info$', InfoView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]