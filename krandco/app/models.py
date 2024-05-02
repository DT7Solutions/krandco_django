from django.db import models
from datetime import datetime
from import_export import resources, fields


# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=100)
    Comments = models.CharField(max_length=500,null=False)

    def __str__(self):
        return self.Name

# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )
# class ImageCategorys(models.Model):
#     Name = models.CharField(max_length=100)
#     Image = models.ImageField(upload_to='category_images/')
#     Created = models.DateTimeField(default=datetime.now)

#     def __str__(self):
#         return self.Name  # Return the Name field as the string representation

#     class Meta:
#         verbose_name ='Image Category'
#         verbose_name_plural = 'Image Categories'


# STATUS = (
#     (0,"Draft"),
#     (1,"Publish")
# )

class ProductItem(models.Model):
    Title =  models.CharField(max_length=225,default="")
    Planting = models.CharField(max_length=100)
    Marketing = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    Leaf_Size= models.CharField(max_length=100)
    Volume  = models.CharField(max_length=100)
    Filling_Value = models.CharField(max_length=100)
    Nicotine  = models.CharField(max_length=100)
    Reducing_Sugars = models.CharField(max_length=100)
    Chloride  = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='uploads/')

   
    def __str__(self):
            return self.Title
    

