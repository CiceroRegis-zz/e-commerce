from django.db import models
from filebrowser.fields import FileBrowseField

# Create your models here.


class Product(models.Model):  # product_category

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image = FileBrowseField('products/', max_length=200, null=True, blank=False)

    def __str__(self):
        return self.title
