from django.contrib import admin
from .models import Contact

# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display=['Name','Email','Phone','Address','Comments']

admin.site.register(Contact,AdminContact)

