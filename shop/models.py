from django.db import models
from django.utils.translation import gettext_lazy as _
import webcolors

from ckeditor.fields import RichTextField
from colorfield.fields import ColorField


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('brand'))

    class Meta:
        verbose_name_plural = _('Brand')
        verbose_name = _('brand')

    def __str__(self):
        return self.name


class Color(models.Model):
    model_name = models.CharField(max_length=255, verbose_name=_('model_name'))
    color = models.CharField(max_length=100,  verbose_name=_('color'))
    image = models.ImageField(upload_to='image',  verbose_name=_('image color'))
    hex_code = ColorField(verbose_name=_('hex_code'))  # For storing the color code, e.g., #FF5733

    class Meta:
        verbose_name_plural = _('Color')
        verbose_name = _('Color')

    def __str__(self):
        return f"{self.color}  |  {self.model_name}"

    def save(self, *args, **kwargs):
        if not self.hex_code:
            try:
                self.hex_code = webcolors.name_to_hex(self.color)
            except ValueError:
                self.hex_code = '#000000'  # default to black if color name is not found
        super().save(*args, **kwargs)


class GalleryImage(models.Model):
    product = models.ForeignKey('Mobile', related_name='images', on_delete=models.CASCADE , verbose_name=_('product'))
    image = models.ImageField(upload_to='gallery/' ,  verbose_name=_('image'))

    class Meta:
        verbose_name_plural = _('GalleryImage')
        verbose_name = _('GalleryImage')

    def __str__(self):
        return f"{self.product}"


class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='brand', verbose_name=_('brand') )
    model_name = models.CharField(max_length=100, verbose_name=_('model_name'), unique=True)
    description = RichTextField(verbose_name=_('description'))
    slug = models.SlugField(verbose_name=_('slug'), unique=True)
    inventory = models.BooleanField(default=False,  verbose_name=_('inventory'))
    
    price = models.DecimalField(max_digits=10, decimal_places=2,  verbose_name=_('price'))
    screen_size = models.CharField(max_length=255, verbose_name=_('screen_size'))
    battery_capacity = models.CharField(max_length=255, verbose_name=_('battery_capacity'))
    camera_resolution = models.CharField(max_length=255, verbose_name=_('camera_resolution'))
    storage_capacity = models.CharField(max_length=255,  verbose_name=_('storage_capacity'))
    ram = models.IntegerField(verbose_name=_('ram'))
    operating_system = models.CharField(max_length=50,  verbose_name=_('operating_system'))
    image_default = models.ImageField(upload_to='image_default',  verbose_name=_('image_default'))  # آدرس عکس پیش‌فرض
    colors = models.ManyToManyField(Color, verbose_name=_('colors'), related_name='colors')
    
    release_date = models.DateField(verbose_name=_('release_date'))

    class Meta:
        verbose_name = _('Mobile')
        verbose_name_plural = _('Mobile')

    def __str__(self):
        return f"{self.brand} {self.model_name}"
    

class Network(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='network',  verbose_name=_('product'))
    technology = models.CharField(max_length=255,  verbose_name=_('technology'))
    bands_2g = models.CharField(max_length=255,  verbose_name=_('bands_2g'))
    bands_3g = models.CharField(max_length=255,  verbose_name=_('bands_3g'))
    bands_4g = models.CharField(max_length=255,  verbose_name=_('bands_4g'))
    bands_5g = models.CharField(max_length=255,  verbose_name=_('bands_5g'))
    speed = models.CharField(max_length=255,  verbose_name=_('speed'))

    class Meta:
        verbose_name = _('Network')
        verbose_name_plural = _('Network')

    def __str__(self):
        return f'{self.product}'


class Memory(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='memory',  verbose_name=_('product'))
    external = models.BooleanField(default=False ,  verbose_name=_('external'))
    internal = models.CharField(max_length=255 ,  verbose_name=_('internal'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('Memory')
        verbose_name_plural = _('Memory')

    def __str__(self):
        return f'{self.product}'


class Body(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='body' ,  verbose_name=_('product'))
    dimensions = models.CharField(max_length=500, verbose_name=_('dimensions'))
    weight = models.CharField(max_length=500, verbose_name=_('weight'))
    build = models.CharField(max_length=500, verbose_name=_('build'))
    sim = models.CharField(max_length=500 , verbose_name=_('sim'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('Body')
        verbose_name_plural = _('Body')

    def __str__(self):
        return f'{self.product}'


class Display(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='display' ,  verbose_name=_('product'))
    type_display = models.CharField(max_length=500, verbose_name=_('type display'))
    resolution = models.CharField(max_length=50, blank=True ,  verbose_name=_('resolution'))
    screen_size = models.CharField(max_length=50, blank=True ,  verbose_name=_('screen_size'))
    anti_shock = models.BooleanField(default=False ,  verbose_name=_('anti_shock'))
    refresh_rate = models.CharField(max_length=50, blank=True ,  verbose_name=_('refresh_rate'))
    screen_always_on = models.BooleanField(default=False ,  verbose_name=_('screen_always_on'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('Display')
        verbose_name_plural = _('Display')

    def __str__(self):
        return f'{self.product}'


class Function(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='function' ,  verbose_name=_('product'))
    os = models.CharField(max_length=500, verbose_name=_('os'))
    cpu = models.CharField(max_length=500,  verbose_name=_('cpu'))
    gpu = models.CharField(max_length=500, verbose_name=_('gpu') )
    chipset = models.CharField(max_length=500, verbose_name=_('chipset'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('Function')
        verbose_name_plural = _('Function')

    def __str__(self):
        return f'{self.product}'


class MainCamera(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.PROTECT, related_name='maincamera',  verbose_name=_('product'))
    camera = models.CharField(max_length=550, verbose_name=_('camera'))
    features = models.CharField(max_length=500, verbose_name=_('features'))
    video = models.CharField(max_length=500, verbose_name=_('video'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('mainCamera')
        verbose_name_plural = _('MainCamera')

    def __str__(self):
        return f'{self.product}'


class SelfieCamera(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.PROTECT, related_name='selficamera', verbose_name=_('product'))
    camera = models.CharField(max_length=550, verbose_name=_('camera'))
    features = models.CharField(max_length=500, verbose_name=_('features'))
    video = models.CharField(max_length=500, verbose_name=_('video'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('SelfieCamera')
        verbose_name_plural = _('SelfieCamera')

    def __str__(self):
        return f'{self.product}'


class Sound(models.Model):
    product = models.OneToOneField(Mobile,on_delete=models.CASCADE, related_name='sound' ,  verbose_name=_('product'))
    speaker_type = models.CharField( max_length=500 ,  verbose_name=_('speaker_type'))
    jack_35_milimetr = models.BooleanField(default=False ,  verbose_name=_('jack_35_milimetr'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('Sound')
        verbose_name_plural = _('Sound')

    def __str__(self):
        return f'{self.product}'


class Battery(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='battery' ,  verbose_name=_('product'))
    type_battery = models.CharField(max_length=500, verbose_name=_('type battery'))
    charging = models.CharField(max_length=500, verbose_name=_('charging'))
    battry_replacement = models.BooleanField(default=False ,  verbose_name=_('battry replacement'))
    wierles_charge = models.BooleanField(default=False,  verbose_name=_('wierles charge'))
    fats_charge = models.BooleanField(default=False,  verbose_name=_('fats charge'))
    time_charge = models.CharField(max_length=500, verbose_name=_('time charge'))
    otg_support = models.BooleanField(default=False, verbose_name=_('otg support'))
    max_wattage = models.CharField(max_length=225, verbose_name=_('max wattage'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('Battery')
        verbose_name_plural = _('Battery')

    def __str__(self):
        return f'{self.product}'


class OtherFeatures(models.Model):
    product = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='ortherfeatures',  verbose_name=_('product'))
    nfc = models.BooleanField(default=False, verbose_name=_('nfc'))
    simcard = models.CharField(max_length=500,  verbose_name=_('simcard'))
    bakup_5g = models.BooleanField(default=False,  verbose_name=_('bakup_5g'))
    multiple_user = models.BooleanField(default=False ,  verbose_name=_('multiple_user'))
    version_usb = models.PositiveIntegerField(default=0 ,  verbose_name=_('version_usb'))
    gps = models.BooleanField(default=False,  verbose_name=_('gps'))
    wifi = models.CharField(max_length=500,  verbose_name=_('wifi'))
    sensors = models.CharField(max_length=500, verbose_name=_('sensor'))
    voice_command = models.BooleanField(default=False ,  verbose_name=_('voice_command'))
    hotspot = models.BooleanField(default=False,  verbose_name=_('hotspot'))
    language_support = models.PositiveIntegerField(default=0,  verbose_name=_('language_support'))
    version_bluetooth = models.CharField(max_length=50, blank=True ,  verbose_name=_('version_bluetooth'))
    support_persian = models.BooleanField(default=False,  verbose_name=_('support_persian'))
    other = models.CharField(max_length=500, blank=True, verbose_name=_('other'))

    class Meta:
        verbose_name = _('OtherFeatures')
        verbose_name_plural = _('OtherFeatures')

    def __str__(self):
        return f'{self.product}'
    

class SliderImage(models.Model):
    title = models.CharField(max_length=100 ,  verbose_name=_('title'))
    description = models.TextField(   verbose_name=_('description'))
    image = models.ImageField(upload_to='media/slider_images' ,  verbose_name=_('image'))
    is_active = models.BooleanField(default=True ,  verbose_name=_('is_active'))

    class Meta:
        verbose_name = _('SliderImage')
        verbose_name_plural = _('SliderImage')

    def __str__(self):
        return self.title
