from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.manager import Manager

class ActiveBookManager(models.Manager):
    def get_queryset(self): #Books.objects.all()
        return super().get_queryset().filter(is_deleted='N')

class InActiveBookManager(models.Manager):
    def get_queryset(self): #Books.objects.all()
        return super().get_queryset().filter(is_deleted='Y')

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length=1, default="N")
    active_books = ActiveBookManager() # CustomManager--substitute of objects
    inactive_books = InActiveBookManager()
    objects = Manager()

    def __str__(self):
        return f'{self.__dict__}' 

    class Meta:
        db_table = 'book'