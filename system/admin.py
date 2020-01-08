from django import forms
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse
from guardian.admin import GuardedModelAdmin
from mptt.admin import DraggableMPTTAdmin
from mptt.forms import TreeNodeChoiceField

from system.models import Organization, Role, User, Group

admin.site.site_title = "后台管理"
admin.site.site_header = "后台管理"
admin.site.index_title = "后台管理"

# class OrganizationInlineForm(forms.ModelForm):
#     tree_field = TreeNodeChoiceField(queryset=Organization.objects.all())
#
#
# class UserInline(admin.TabularInline):
#     model = Organization
#     form = OrganizationInlineForm
#     extra = 1


@admin.register(User)
class UserInfoAdmin(UserAdmin, GuardedModelAdmin):
    fieldsets = (
        ('Personal info', {'fields': ('username', 'password', 'avatar', 'nickname', 'phone', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'organization', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'created_time')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'organization'),
        }),
    )

    readonly_fields = ('last_login', 'created_time')
    list_display = ('username', 'avatar', 'phone', 'email', 'organization')
    list_filter = ('is_active', 'is_staff', 'groups', 'organization',)
    search_fields = ('username', 'phone', 'nickname')
    date_hierarchy = 'created_time'
    actions_selection_counter = True
    list_editable = ('phone', 'email',)
    list_per_page = 100
    save_on_top = False
    view_on_site = True

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name == 'organization':
    #         field = TreeNodeChoiceField(
    #             required=False,
    #             queryset=User.organization,
    #             level_indicator=u'---',
    #         )
    #     else:
    #         field = super(UserInfoAdmin, self).formfield_for_dbfield(
    #             db_field, **kwargs)
    #     return field


@admin.register(Organization)
class OrganizationAdmin(DraggableMPTTAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'parent', 'desc')})
    ]
    list_display = ('tree_actions', 'indented_title', 'desc', 'created_time', 'updated_time',)
    list_filter = ('created_time', 'updated_time',)
    search_fields = ('name',)
    list_display_links = ('indented_title',)
    mptt_level_indent = 20

    def delete_selected_tree(self, modeladmin, request, queryset):
        try:
            return super().delete_selected_tree(modeladmin, request, queryset)
        except ProtectedError:
            msg = "You cannot delete an object with children"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name == 'parent':
    #         field = TreeNodeChoiceField(
    #             required=False,
    #             queryset=Organization.objects.all(),
    #             level_indicator=u'+--',
    #         )
    #     else:
    #         field = super(OrganizationAdmin, self).formfield_for_dbfield(
    #             db_field, **kwargs)
    #     return field


@admin.register(Role)
class RoleAdmin(DraggableMPTTAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'parent', 'desc', 'permissions')})
    ]
    list_display = ('tree_actions', 'indented_title', 'desc', 'created_time', 'updated_time',)
    list_filter = ('created_time', 'updated_time',)
    search_fields = ('name',)
    list_display_links = ('indented_title',)
    mptt_level_indent = 20
    filter_horizontal = ('permissions',)

    def delete_selected_tree(self, modeladmin, request, queryset):
        try:
            return super().delete_selected_tree(modeladmin, request, queryset)
        except ProtectedError:
            msg = "You cannot delete an object with children"
            self.message_user(request, msg, messages.ERROR)
            opts = self.model._meta
            return_url = reverse(
                'admin:%s_%s_changelist' % (opts.app_label, opts.model_name),
                current_app=self.admin_site.name,
            )
            return HttpResponseRedirect(return_url)


@admin.register(Group)
class GroupInfoAdmin(GroupAdmin, DraggableMPTTAdmin):
    fieldsets = [
        (None, {'fields': ('name', 'parent', 'desc', 'roles', 'permissions')})
    ]
    filter_horizontal = ('roles', 'permissions',)

