from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class TypeAwards(models.Model):
    type_awards_id = models.IntegerField(primary_key=True)
    type_awards = models.CharField(max_length=100)

    class Meta:
        db_table = 'type_awards'  # Имя существующей таблицы


class Awards(models.Model):
    awards_id = models.IntegerField(primary_key=True)
    awards_name = models.CharField(max_length=300)
    fk_type_awards = models.ForeignKey(TypeAwards, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = 'awards'

    def __str__(self):
        return self.awards_name


class Employee(models.Model):
    emplyees_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    fk_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    fk_awards = models.ForeignKey(Awards, on_delete=models.CASCADE, blank=True)
    hire = models.IntegerField()
    kgtu_hire = models.IntegerField()
    experience = models.IntegerField()
    kgtu_experience = models.IntegerField()

    class Meta:
        db_table = 'employees'  # Имя существующей таблицы


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'post'  # Имя существующей таблицы

    def __str__(self):
        return self.post_name


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=200, verbose_name="Имя и фамилия", null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, verbose_name="Email",null=True, blank=True)
    phone = models.CharField(max_length=255, unique=True, verbose_name="Phone",null=True, blank=True)

