from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from mebel_sayt.models import Product
from .forms import ProductForm


@staff_member_required(login_url='dash_log')
def prod_add_edit(request, pk=None):
    forms = ProductForm()
    if pk:
        ctg = Product.objects.get(pk=pk)
        forms = ProductForm(instance=ctg)
    else:
        ctg = None
    if request.POST:
        if pk:
            form = ProductForm(request.POST, request.FILES or None, instance=ctg)
        else:
            form = ProductForm(request.POST, request.FILES or None)

        if form.is_valid():
            form.save()
            return redirect("dashboard_prod_list")
        else:
            print(form.errors)
    ctx = {
        'forms': forms
    }
    return render(request, 'dashboard/product/form.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_list(request):
    ctgs = Product.objects.all()
    ctx = {
        'ctgs': ctgs
    }
    return render(request, 'dashboard/product/list.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_detail(request, pk):
    ctg = Product.objects.get(pk=pk)
    ctx = {
        'ctg': ctg
    }
    return render(request, 'dashboard/product/detail.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_del_conf(request, pk):
    ctg = Product.objects.get(pk=pk)
    ctx = {
        'ctg': ctg
    }
    return render(request, 'dashboard/product/delete.html', ctx)


@staff_member_required(login_url='dash_log')
def prod_delete(request, pk):
    ctg = Product.objects.get(pk=pk).delete()
    return redirect('dashboard_prod_list')
