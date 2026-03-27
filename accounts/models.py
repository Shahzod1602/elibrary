from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=100, verbose_name="First name")
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    direction = models.CharField(max_length=200, verbose_name="Major")
    group = models.CharField(max_length=100, verbose_name="Group")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Phone number")
    id_number = models.CharField(max_length=50, unique=True, null=True, blank=True, verbose_name="ID number")
    photo_image = models.ImageField(
        upload_to='student_photos/', blank=True, null=True, verbose_name="Photo image"
    )

    class Meta:
        verbose_name = "Student profile"
        verbose_name_plural = "Student profiles"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.user.username})"
