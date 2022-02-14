from operator import truediv
from sre_parse import State
from turtle import title
from django.db import models
from django.db.models.fields import SlugField, CharField, IntegerField, DateTimeField
from django.db.models import ImageField
from django.db.models.fields.related import ManyToManyField, ForeignKey

# Create your models here.

LIST_STATE = (
    {0, "disable"},
    {1, "enable"}
)

PIZZA_TYPE = (
    {0, "Pizza"},
    {1, "Slice"},
    {2, "Roll"},


)

class Pizza(models.Model):
    type = ForeignKey('Type', on_delete=models.SET_NULL, null=True, blank=True)
    title = CharField(max_length=150, unique=True,null=True,blank=True)
    slug = SlugField(unique=True, db_index=True, null=True, blank=True)
    price = IntegerField(default=1)
    picture = ImageField(null=True, upload_to="pizza/")
    state = IntegerField(default=0, choices=LIST_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    ingredients = ManyToManyField('Ingredient')
    # type = IntegerField(default=0, choices=PIZZA_TYPE)

    def __str__(self) :
        return self.title


class Type(models.Model):
    # type = IntegerField(default=0, choices=PIZZA_TYPE)
    type = CharField(max_length=80, unique=True)
    slug = SlugField(unique=True, db_index=True, null=True, blank=True)
    state = IntegerField(default=0, choices=LIST_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class Command(models.Model):
    pizza = ManyToManyField('Pizza')
    nbrp = IntegerField(default=1, )
    total = IntegerField()
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)



class Ingredient(models.Model):
    title = CharField(max_length=100)
    slug = SlugField(unique=True, db_index=True, null=True, blank=True)
    state = IntegerField(default=0, choices=LIST_STATE)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)


    def __str__(self) :
        return self.title

