from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.translation import gettext_lazy as _

from . import models

admin.site.site_header = 'mobile store'
admin.site.index_title = 'admin store'


@admin.register(models.Mobile)
class MobileAdmin(admin.ModelAdmin):
    model = models.Mobile
    list_display = ['brand', 'model_name', 'release_date', 'price', 'inventory']
    list_editable = ['price','inventory']
    list_filter = ['brand', 'model_name', 'release_date', 'inventory']
    prepopulated_fields = {
        'slug': ['model_name', ]
    }


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'count_mobile']
    list_per_page = 10
    list_filter = ['name', ]

    def get_queryset(self, request):
        return super() \
            .get_queryset(request) \
            .prefetch_related('brand') \
            .annotate(count_mobile=Count('brand'))

    @admin.display(description=_('count mobile'), ordering='count_mobile')
    def count_mobile(self, obj):
        url = (reverse('admin:shop_mobile_changelist')
               + '?'
               + urlencode({'brand_id': obj.id})

               )
        return format_html('<a href="{}">{}</a>', url, obj.count_mobile)


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'color']


@admin.register(models.GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    model = models.GalleryImage
    list_display = ['product', ]



@admin.register(models.Network)
class NetworkAdmin(admin.ModelAdmin):
    model = models.Network


@admin.register(models.SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    model = models.SliderImage


@admin.register(models.Battery)
class BatteryAdmin(admin.ModelAdmin):
    model = models.Battery


@admin.register(models.MainCamera)
class MainCameraAdmin(admin.ModelAdmin):
    model = models.MainCamera


@admin.register(models.SelfieCamera)
class SelfieCameraAdmin(admin.ModelAdmin):
    model = models.SelfieCamera


@admin.register(models.Display)
class DisplayAdmin(admin.ModelAdmin):
    model = models.Display


@admin.register(models.OtherFeatures)
class OtherFeatures(admin.ModelAdmin):
    model = models.OtherFeatures


@admin.register(models.Sound)
class SoundAdmin(admin.ModelAdmin):
    model = models.Sound


@admin.register(models.Body)
class BodyAdmin(admin.ModelAdmin):
    model = models.Body


@admin.register(models.Memory)
class MemoryAdmin(admin.ModelAdmin):
    model = models.Memory
