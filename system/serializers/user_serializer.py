from rest_framework import serializers, viewsets

from system.models import User
from system.serializers.group_serializer import GroupSerializer
from system.serializers.organization_serializer import OrganizationSerializer
from system.serializers.permission_serializer import PermissionSerializer


class UserSerializer(serializers.ModelSerializer):

    organization = OrganizationSerializer()
    groups = GroupSerializer(many=True)
    user_permissions = PermissionSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer



