from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from ProductApp.models import *
from UserApp.models import *
from ProductApp.forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(redirect_field_name='')
def all_doc(request):
    doc_type = request.GET.get('doc_type')
    # Get Purchase All Order
    purchase_order = PurchaseOrder.objects.filter(doc_type=doc_type)
    table_header = {
        'display_only': ['Number'],
        'not_display_only': ['Date', 'Company', 'Status'],
    }
    # Menu Active
    nav = 'invoice' if doc_type == 'inv' else 'purchase_order'
    nav_active = {
        nav : 'active',
    }
    # Title Page
    title = 'List {}'.format('Invoice' if doc_type == 'inv' else 'Purchase Order')
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': title,
        'menu_active': nav_active,
        'table_header': table_header,
        'purchase_order': purchase_order,
        'position': 'Invoice',
        'doc_type': doc_type,
        'biouser': biouser,
    }
    return render(request, 'datatable/all_po.html', context)    


@login_required(redirect_field_name='')
def add_doc(request):
    doc_type = request.GET.get('doc_type')
    if request.method == 'POST':
        # Initialization Purchase Order And Save
        number = request.POST.get('number')
        try:
            po_form = PurchaseOrderForm(request.POST or None)
            if po_form.is_valid():
                po_form.create(doc_type)
            # Initialization Order And Save
            products = request.POST.getlist('product')
            quantities = request.POST.getlist('quantity')
            length = min([len(products), len(quantities)])
            for i in range(length):
                order_form = OrderForm({'product': products[i], 'quantity': quantities[i]})
                if order_form.is_valid():
                    order_form.create(number)
            messages.success(request, 'Data saved successfully')
        except:
            purchase_order = PurchaseOrder.objects.get(number=number)
            purchase_order.delete()
            messages.error(request, 'Please check the form again carefully')
        
        # Redirect To Add New Product
        params = f'doc_type={doc_type}'
        return redirect(reverse('productapp:add-doc') + '?' + params)
    po_form = PurchaseOrderForm()
    order_form = OrderForm()
    list_product = [product['name'] for product in Product.objects.values('name')]
    list_suplier = [suplier['name'] for suplier in Suplier.objects.values('name')]
    # Menu Active
    nav = 'invoice' if doc_type == 'inv' else 'purchase_order'
    nav_active = {
        nav : 'active',
    }
    # Title Page and Doc
    title = 'Add {}'.format('Invoice' if doc_type == 'inv' else 'Purchase Order')
    title_doc = 'INVOICE' if doc_type == 'inv' else 'PURCHASE ORDER'
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': title,
        'menu_active': nav_active,
        'po_form': po_form,
        'order_form': order_form,
        'list_product': list_product,
        'list_suplier': list_suplier,
        'title_doc': title_doc,
        'biouser': biouser,
    }
    return render(request, 'form/add_po.html', context)


@login_required(redirect_field_name='')
def edit_doc(request):
    doc_id = request.GET.get('doc_id')
    doc_type = request.GET.get('doc_type')
    if request.method == 'POST':
        # Initialization Purchase Order And Save
        number = request.POST.get('number')
        try:
            po_form = PurchaseOrderForm(request.POST or None)
            if po_form.is_valid():
                po_form.update(doc_id)
                # Delete Old Order
                po = PurchaseOrder.objects.get(custom_id=doc_id)
                order_list = Order.objects.filter(number=po)
                for odr in order_list:
                    order = Order.objects.get(id=odr.id)
                    order.delete()
            # Initialization Order And Save
            products = request.POST.getlist('product')
            quantities = request.POST.getlist('quantity')
            length = min([len(products), len(quantities)])
            for i in range(length):
                order_form = OrderForm({'product': products[i], 'quantity': quantities[i]})
                if order_form.is_valid():
                    order_form.create(number)
            messages.success(request, 'Data saved successfully')
        except:
            messages.error(request, 'Please check the form again carefully')
        
        # Redirect To Edit This Document
        params = f'doc_id={doc_id}&doc_type={doc_type}'
        return redirect(reverse('productapp:edit-doc') + '?' + params)
    
    # Get Purchase Order Object with ID from Request
    purchase_order = PurchaseOrder.objects.get(custom_id=doc_id)
    # Get Purchase Order Property Value from Object
    data_po = {
        'status': purchase_order.status,
        'number': purchase_order.number,
        'company': purchase_order.company,
        'name': purchase_order.name,
        'address': purchase_order.address,
        'note': purchase_order.note,
    }
    # Initial Purchase Order Property Value To Form
    po_form = PurchaseOrderForm(request.POST or None, initial=data_po)
    # Disabled One of Field in Purchase Order Form
    list_order_form = []
    data_send = []
    # Get Order Object Linked to Purchase Order Object
    list_order = Order.objects.filter(number=purchase_order)
    for order in list_order:
        order = Order.objects.get(id=order.id)
        data_order = {
            'product': order.product,
            'quantity': order.quantity,
        }
        form = OrderForm(request.POST or None, initial=data_order)
        list_order_form.append(form)
        data_send.append(order.product.purchase)
    order_form = OrderForm()
    edit = True
    list_product = [product['name'] for product in Product.objects.values('name')]
    list_suplier = [suplier['name'] for suplier in Suplier.objects.values('name')]
    # Menu Active
    nav = 'invoice' if doc_type == 'inv' else 'purchase_order'
    nav_active = {
        nav : 'active',
    }
    # Title Page and Doc
    title = 'Edit {}'.format('Invoice' if doc_type == 'inv' else 'Purchase Order')
    title_doc = 'INVOICE' if doc_type == 'inv' else 'PURCHASE ORDER'
    biouser = BioUser.objects.get(user=request.user)
    # Data Send In Template
    context = {
        'title': title,
        'menu_active': nav_active,
        'po_form': po_form,
        'order_form': order_form,
        'list_product': list_product,
        'list_suplier': list_suplier,
        'list_order_form': list_order_form,
        'edit': edit,
        'data_send': data_send,
        'title_doc': title_doc,
        'biouser': biouser,
    }
    return render(request, 'form/add_po.html', context)


@login_required(redirect_field_name='')
def del_doc(request):
    doc_type = request.GET.get('doc_type')
    doc_id = request.GET.get('doc_id')
    doc_id = doc_id.split("+")
    for one_id in doc_id:
        one_id = int(one_id)
        purchase_order = PurchaseOrder.objects.get(id=one_id)
        purchase_order.delete()
    params = f'doc_type={doc_type}'
    return redirect(reverse('productapp:all-doc') + '?' + params)



# Product Function ------------------------------------------------------------------------------------------
@login_required(redirect_field_name='')
def all_product(request):
    product_list = Product.objects.all()
    table_header = {
        'display_only': ['Name'],
        'not_display_only': ['Purchase', 'Selling', 'Stock'],
    }
    nav_active = {
        'products': 'active',
    }
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': 'List Products',
        'menu_active': nav_active,
        'product_list': product_list,
        'table_header': table_header,
        'biouser': biouser,
    }
    return render(request, 'datatable/all_product.html', context)


@login_required(redirect_field_name='')
def add_product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST or None)
        print(product_form.is_valid())
        if product_form.is_valid():
            product_form.create()
            messages.success(request, 'Data saved successfully')
            return redirect('productapp:add-product')
        else:
            messages.error(request, 'Please check the form again carefully')
    product_form = ProductForm()
    nav_active = {
        'products': 'active',
    }
    add = True
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': 'Add Products',
        'menu_active': nav_active,
        'product_form': product_form,
        'add' : add,
        'biouser': biouser,
    }
    return render(request, 'form/add_product.html', context)


@login_required(redirect_field_name='')
def edit_product(request, product_id):
    product = Product.objects.get(custom_id=product_id)
    data = {
        'name': product.name,
        'number': product.number,
        'purchase': product.purchase,
        'selling': product.selling,
        'stock': product.stock,
        'descriptions': product.descriptions,
        'company': product.company
    }
    product_form = ProductForm(request.POST or None, initial=data)
    if request.method == "POST":
        product_form = ProductForm(request.POST or None)
        if product_form.is_valid():
            product_form.update(product.custom_id)
            messages.success(request, 'Data saved successfully')
            return redirect('productapp:edit-product', product_id)
        else:
            messages.error(request, 'Please check the form again carefully')

    nav_active = {
        'product': 'active',
    }
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': 'Edit Product',
        'menu_active': nav_active,
        'product_form': product_form,
        'biouser': biouser,
    }
    return render(request, 'form/add_product.html', context)

@login_required(redirect_field_name='')
def del_product(request, product_id):
    product_id = product_id.split("+")
    for one_id in product_id:
        one_id = int(one_id)
        product = Product.objects.get(id=one_id)
        product.delete()
    return redirect('productapp:all-product')


# Suplier Function ------------------------------------------------------------------------------------------
@login_required(redirect_field_name='')
def all_suplier(request):
    suplier_list = Suplier.objects.all()
    table_header = {
        'display_only': ['Name'],
        'not_display_only': ['Suplier', 'Email'],
    }
    nav_active = {
        'suplier': 'active',
    }
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': 'List Suplier',
        'menu_active': nav_active,
        'suplier_list': suplier_list,
        'table_header': table_header,
        'biouser': biouser,
    }
    return render(request, 'datatable/all_suplier.html', context)


#Function For Add Suplier Object
@login_required(redirect_field_name='')
def add_suplier(request):
    if request.method == "POST":
        # Get Suplier Form Property Value From Request And Save
        suplier_form = SuplierForm(request.POST or None)
        if suplier_form.is_valid():
            suplier_form.create()
            messages.success(request, 'Data saved successfully')
            return redirect('productapp:add-suplier')
        else:
            # Message For Error
            messages.error(request, 'Please check the form again carefully')
    
    suplier_form = SuplierForm()
    # Dictionary For Navigation Active
    nav_active = {
        'suplier': 'active',
    }
    biouser = BioUser.objects.get(user=request.user)
    # Dictionary For Send To Template View
    context = {
        'title': 'Add Suplier',
        'menu_active': nav_active,
        'suplier_form': suplier_form,
        'biouser': biouser,
    }
    return render(request, 'form/add_suplier.html', context)


#Function For Edit Suplier Object
@login_required(redirect_field_name='')
def edit_suplier(request, suplier_id):
    # Get Suplier Object With Request in ID
    suplier = Suplier.objects.get(custom_id=suplier_id)

    # Get Suplier Property Value From Suplier Object
    data = {
        'name': suplier.name,
        'suplier': suplier.suplier,
        'email': suplier.email,
        'address': suplier.address,
    }

    # Initialization Suplier Property Value Into Suplier Form
    suplier_form = SuplierForm(request.POST or None, initial=data)
    if request.method == "POST":
        if suplier_form.is_valid():
            suplier_form.update(suplier.custom_id)
            messages.success(request, 'Data saved successfully')
            return redirect('productapp:edit-suplier', suplier_id)
        else:
            messages.error(request, 'Please check the form again carefully')
    # Dictionary For Navigation Active
    nav_active = {
        'suplier': 'active',
    }
    biouser = BioUser.objects.get(user=request.user)
    # Dictionary For Send To Template View
    context = {
        'title': 'Add Suplier',
        'menu_active': nav_active,
        'suplier_form': suplier_form,
        'biouser': biouser,
    }
    return render(request, 'form/add_suplier.html', context)

#Function For Delete Suplier Object
@login_required(redirect_field_name='')
def del_suplier(request, suplier_id):
    # String Suplier ID Into List
    suplier_id = suplier_id.split("+")
    for one_id in suplier_id:
        one_id = int(one_id)
        # Get Suplier Object And Delete It
        suplier = Suplier.objects.get(id=one_id)
        suplier.delete()
    
    # If Success Delete, Then Redirect To List Suplier
    return redirect('productapp:all-suplier')


# Ajax Function ------------------------------------------------------------------------------------------
@login_required(redirect_field_name='')
def get_data(request):
    if request.is_ajax and request.method == "GET":
        # If Ajax Get Product
        if request.GET.get("product", None):
            product = request.GET.get("product", None)
            if Product.objects.filter(name=product).exists():
                product_object = Product.objects.get(name=product)
                product_desc = product_object.descriptions
                product_price = product_object.purchase
                return JsonResponse({
                    'purchase': product_price,
                }, status=200)
            else:
                return JsonResponse({}, status=200)

        # If Ajax Get Suplier
        elif request.GET.get("suplier", None):
            suplier = request.GET.get("suplier", None)
            if Suplier.objects.filter(name=suplier).exists():
                suplier_object = Suplier.objects.get(name=suplier)
                suplier_suplier = suplier_object.suplier
                suplier_email = suplier_object.email
                suplier_address = suplier_object.address
                return JsonResponse({
                    'suplier': suplier_suplier,
                    'email': suplier_email,
                    'address': suplier_address,
                }, status=200)
            else:
                return JsonResponse({}, status=200)

        # If Ajax Get Number Purchase Order
        elif request.GET.get("number-po", None):
            number_po = request.GET.get("number-po", None)
            if PurchaseOrder.objects.filter(number=number_po).exists(): 
                return JsonResponse({'valid': False}, status=200)
            else:
                return JsonResponse({'valid': True}, status=200)
        
        # If Ajax Get Number Invoice
        elif request.GET.get("number-inv", None):
            number_inv = request.GET.get("number-inv", None)
            if PurchaseOrder.objects.filter(number=number_inv).exists(): 
                return JsonResponse({'valid': False}, status=200)
            else:
                return JsonResponse({'valid': True}, status=200)

        # If Error Request
        return JsonResponse({}, status=400)

# Single Document Function ------------------------------------------------------------------------------------------
@login_required(redirect_field_name='')
def single_doc(request):
    return redirect('error')