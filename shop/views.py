from django.shortcuts import render, get_object_or_404, redirect
from .models import Mobile , SliderImage



def mobile_list(request):
    products = Mobile.objects.all()
    slider_images = SliderImage.objects.filter(is_active=True)
   
    return render(request, 'mobile_list.html', {'products': products,'slider_images': slider_images})


def product_detail(request, slug):
    product = get_object_or_404(Mobile,slug=slug)
    similar_products = Mobile.objects.filter(brand=product.brand).exclude(pk=product.pk)[:3]

    context = {
        'product': product,
        'similar_products': similar_products,
    }
    return render(request, 'product_detail.html', context)


