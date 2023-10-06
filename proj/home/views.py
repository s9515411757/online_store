from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


from .models import Product
from .forms import ProductForm


def index(request):

    products = Product.objects.order_by('-pub_date')[:10]
    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)


@login_required
def product_edit(request, post_id):
    post = get_object_or_404(
        Product.objects.select_related('author'), pk=post_id
    )
    if request.user != post.author:
        return redirect('home:post_detail', post.id)

    form = ProductForm(
        request.POST or None,
        files=request.FILES or None,
        instance=post
    )

    if form.is_valid():
        form.save()
        return redirect('home:post_detail', post.id)

    context = {
        'form': form,
        'is_edit': True
    }
    return render(request, 'home/create_product.html', context)


@login_required
def product_create(request):
    form = ProductForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        return redirect('home:index')

    context = {
        'form': form,
        'is_edit': False
    }
    return render(request, 'home/create_product.html', context)