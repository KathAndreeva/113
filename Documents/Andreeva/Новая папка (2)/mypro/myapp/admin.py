from django.contrib import admin

# Register your models here.

from myapp.models import product


class myconfigprod(admin.ModelAdmin):

    list_display = ["name", "count", "cost", "dot"]


admin.site.register(product, myconfigprod)
