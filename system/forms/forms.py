from django import forms
from mptt.forms import TreeNodeChoiceField



# class UserListForm(forms.Form):
#     organization = TreeNodeChoiceField(queryset=User.organization.objects.all())
#
#     class Meta:
#         model = User
from system.models import Organization



