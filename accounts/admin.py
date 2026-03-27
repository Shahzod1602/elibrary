from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import StudentProfile


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    direction = forms.CharField(max_length=200, required=True, label="Major")
    group = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=20, required=False, label="Phone number")
    id_number = forms.CharField(max_length=50, required=True, label="ID number")
    photo_image = forms.ImageField(required=False, label="Photo image")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            StudentProfile.objects.update_or_create(
                user=user,
                defaults={
                    "first_name": self.cleaned_data["first_name"],
                    "last_name": self.cleaned_data["last_name"],
                    "direction": self.cleaned_data["direction"],
                    "group": self.cleaned_data["group"],
                    "phone": self.cleaned_data.get("phone", ""),
                    "id_number": self.cleaned_data["id_number"],
                    "photo_image": self.cleaned_data.get("photo_image"),
                },
            )
        return user


class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    verbose_name = "Student profile details"
    fields = (
        'first_name',
        'last_name',
        'direction',
        'group',
        'phone',
        'id_number',
        'photo_image',
    )


class UserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    inlines = (StudentProfileInline,)
    list_display = (
        'username',
        'email',
        'get_full_name',
        'get_id_number',
        'get_direction',
        'get_group',
        'get_phone',
        'is_active',
    )
    list_filter = ('is_active', 'is_staff')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'first_name',
                'last_name',
                'direction',
                'group',
                'phone',
                'id_number',
                'photo_image',
                'password1',
                'password2',
            ),
        }),
    )

    def get_full_name(self, obj):
        try:
            p = obj.student_profile
            return f"{p.last_name} {p.first_name}"
        except StudentProfile.DoesNotExist:
            return '-'
    get_full_name.short_description = "Full name"

    def get_id_number(self, obj):
        try:
            return obj.student_profile.id_number
        except StudentProfile.DoesNotExist:
            return '-'
    get_id_number.short_description = "ID number"

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
