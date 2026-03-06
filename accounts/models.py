from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    first_name = models.CharField(max_length=100, verbose_name="Ism")
    last_name = models.CharField(max_length=100, verbose_name="Familiya")
    direction = models.CharField(max_length=200, verbose_name="Yo'nalish")
    group = models.CharField(max_length=100, verbose_name="Guruh")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon raqami")

    class Meta:
        verbose_name = "Talaba profili"
        verbose_name_plural = "Talaba profillari"

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.user.username})"
