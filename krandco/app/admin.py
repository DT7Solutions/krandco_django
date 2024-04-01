from django.contrib import admin
from .models import Contact,Product

# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display=['Name','Email','Phone','Address','Comments']

admin.site.register(Contact,AdminContact)


class AdminProduct(admin.ModelAdmin):
    list_display=('Id','Title','Create_at')
    list_filter = ['Create_at']

admin.site.register(Product,AdminProduct)


