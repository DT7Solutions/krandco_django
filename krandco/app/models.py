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

class Productitem(models.Model):
    # Id = models.AutoField(primary_key=True)
    Title =  models.CharField(max_length=225,default="title")
    # ImageCategory = models.ForeignKey(ImageCategorys,on_delete=models.CASCADE,related_name='categories')
    # Description = models.CharField(max_length=2000,blank=True,null=True)
    Image1 = models.ImageField(upload_to='uploads/')
    CropYear = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    Grade = models.CharField(max_length=100)
    From = models.CharField(max_length=100)
    Nic = models.CharField(max_length=100)
    Sug = models.CharField(max_length=100)
    Packing = models.CharField(max_length=100)
    Quantity = models.CharField(max_length=100)
    # CreatedName =  models.CharField(max_length=100)
    # Create_at = models.DateTimeField(default=datetime.now)
    # status = models.IntegerField(choices=STATUS, default=0)

    # class Meta:
    #     ordering = ['-Create_at']

    def __str__(self):
            return self.Title
    

