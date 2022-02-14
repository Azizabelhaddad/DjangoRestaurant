from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.db.models import UUIDField, CharField, EmailField, IntegerField, BooleanField,DateTimeField, ImageField,SlugField

# Create your models here.

class Profile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    id = UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    name = CharField(max_length=80, null=True, blank=True)
    username = CharField(max_length=80, null=True, blank=True)
    slug = SlugField( unique=True, db_index=True,null=True, blank=True)
    picture = ImageField(null=True,blank=True, upload_to='profiles/')
    adress = CharField(max_length=100, null=True, blank=True)
    tel = IntegerField(null=True, blank=True)
    email = EmailField(max_length=100, null=True, blank=True)
    state = BooleanField(default=False, choices=((True, 'Enabled'), (False, 'Disabled')))
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)


    def __str__(self):
        return self.username

