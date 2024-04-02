from django.contrib import admin
from .models import Contact,Productitem
from import_export.admin import ImportExportModelAdmin
# from .resources import ProductItemResource

# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display=['Name','Email','Phone','Address','Comments']

admin.site.register(Contact,AdminContact)


class AdminProduct(ImportExportModelAdmin):
    # resource_class = ProductItemResource
    list_display=('Title','CropYear')


admin.site.register(Productitem,AdminProduct)

# class AdminImageCategories(admin.ModelAdmin):
#     list_display=('Image','Created')

# admin.site.register(ImageCategorys,AdminImageCategories)


