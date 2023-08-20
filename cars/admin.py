from django.contrib import admin
from. models import Car
from django.utils.html import format_html
# Register your models here.
class Cars(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:2px" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Car photo'
    list_display=('id','car_title','thumbnail','model','year', 'price','create_date','is_featured',)
    list_display_links=('id','car_title',)
    list_editable=('is_featured',)
    list_search=('id','car_title','model','year','city','fuel_type','description')
    list_filter=('city','fuel_type','model', 'description')
admin.site.register(Car, Cars)
