from django.contrib import admin

# Register your models here.
from .models import product

class productsAdmin(admin.ModelAdmin):
    list_display=['__str__','slug']
    class Meta:
        model=product

admin.site.register(product, productsAdmin)