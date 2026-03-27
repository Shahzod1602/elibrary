from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StudentProfile


class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    verbose_name = "Student profile details"
    fields = ('first_name', 'last_name', 'direction', 'group', 'phone')


class UserAdmin(BaseUserAdmin):
    inlines = (StudentProfileInline,)
    list_display = ('username', 'get_full_name', 'get_direction', 'get_group', 'get_phone', 'is_active')
    list_filter = ('is_active', 'is_staff')

    def get_full_name(self, obj):
        try:
            p = obj.student_profile
            return f"{p.last_name} {p.first_name}"
        except StudentProfile.DoesNotExist:
            return '-'
    get_full_name.short_description = "Full name"

    def get_direction(self, obj):
        try:
            return obj.student_profile.direction
        except StudentProfile.DoesNotExist:
            return '-'
    get_direction.short_description = "Major"

    def get_group(self, obj):
        try:
            return obj.student_profile.group
        except StudentProfile.DoesNotExist:
            return '-'
    get_group.short_description = "Group"

    def get_phone(self, obj):
        try:
            return obj.student_profile.phone
        except StudentProfile.DoesNotExist:
            return '-'
    get_phone.short_description = "Phone"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
