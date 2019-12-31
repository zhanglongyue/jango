from django.conf.urls import url
from django.urls import include

from system.serializers._routers import router

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'user/', UserListView),
]