from django.contrib import admin
from .models import Contact,ProductItem
from import_export.admin import ImportExportModelAdmin
# from import_export.formats.base_formats import XLSX, CSV, JSON

from .resources import ProductItemResource

# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display=['Name','Email','Phone','Address','Comments']

admin.site.register(Contact,AdminContact)


class AdminProduct(ImportExportModelAdmin):
    list_display=['Title','Create_at','CreatedName','Type']
    # formats = [XLSX, CSV, JSON]
    resource_class = ProductItemResource


admin.site.register(ProductItem,AdminProduct)

# class AdminImageCategories(admin.ModelAdmin):
#     list_display=('Image','Created')

# admin.site.register(ImageCategorys,AdminImageCategories)


