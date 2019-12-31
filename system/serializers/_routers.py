from rest_framework import routers

from system.serializers.group_serializer import GroupViewSet
from system.serializers.organization_serializer import OrganizationViewSet
from system.serializers.permission_serializer import PermissionViewSet
from system.serializers.user_serializer import UserViewSet

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'users', UserViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'groups', GroupViewSet)
