from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'user_id', 'email', 'date_of_birth', 'phone',
                    'is_admin')  # 기본 화면에서 보이는 필드셋
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('user_id',  'password',)}),
        ('Personal info', {'fields': ('date_of_birth', 'email',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (  # 데이터 추가할 때 보이는 필드셋
        (None, {
            'classes': ('wide',),
            'fields': ('user_id', 'email', 'date_of_birth', 'phone', 'password1', 'password2')}
         ),
    )

    serach_fields = ('email',)
    ordering = ('id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
