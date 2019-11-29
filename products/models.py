from django.db import models
from filebrowser.fields import FileBrowseField

from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def use(self):
        return self.filter(use=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def useImage(self):
        return self.get_queryset().use()


    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):  # product model

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(
        decimal_places=2, max_digits=20, default=100.00)
    image = FileBrowseField('products', max_length=200, null=True, blank=False)
    slug = models.SlugField(blank=True, unique=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = ProductManager()  # return product by id

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


class CarouselImageHome(models.Model):

    carouselImage = FileBrowseField('carouselImage', max_length=200, null=True, blank=False)
    createAt = models.DateTimeField( null=False, blank=False, editable=False, auto_now_add=True)
    use = models.BooleanField(default=False)

    def __str__(self):
        return format(self.carouselImage)
