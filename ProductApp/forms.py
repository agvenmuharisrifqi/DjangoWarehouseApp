from django import forms
from ProductApp.models import *
from ckeditor.widgets import CKEditorWidget

class SuplierForm(forms.Form):
    name = forms.CharField(
        label='Company Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    suplier = forms.CharField(
        label='Suplier Name',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    email = forms.EmailField(
        label='Suplier Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    address = forms.CharField(
        label='Suplier Address',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )

    def create(self):
        data = self.cleaned_data
        suplier = Suplier(
            name = data['name'],
            suplier = data['suplier'],
            email = data['email'],
            address = data['address']
        )
        suplier.save()

    def update(self, custom_id):
        data = self.cleaned_data
        Suplier.objects.filter(custom_id=custom_id).update(
            name = data['name'],
            suplier = data['suplier'],
            email = data['email'],
            address = data['address']
        )        


class ProductForm(forms.Form):
    name = forms.CharField(
        label='Product Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
                'required': True,
            }
        )
    )
    number = forms.CharField(
        label='Product Number',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
                'required': True,
            }
        )
    )
    purchase = forms.IntegerField(
        label='Purchase Price',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
                'required': True,
            }
        )
    )
    selling = forms.IntegerField(
        label='Selling Price',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    stock = forms.IntegerField(
        label='Stock',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    descriptions = forms.CharField(
        label='Product Descriptions',
        required=False,
        widget=CKEditorWidget(config_name='no_toolbar',)
    )
    CHOICE = tuple(
        (idx['name'], idx['name']) for idx in Suplier.objects.values('name')
    )
    CHOICE_COMPANY = (('', 'Choose product company'),) + CHOICE  
    company = forms.CharField(
        label='Company Product',
        widget=forms.Select(
            choices=CHOICE_COMPANY,
            attrs={
                'class': 'input-normal',
                'required': True,
            }
        )
    )
    def create(self):
        data = self.cleaned_data
        company_object = Suplier.objects.get(name=data['company'])
        product = Product(
            name = data['name'],
            number = data['number'],
            purchase = data['purchase'],
            selling = data['selling'],
            stock = data['stock'],
            descriptions = data['descriptions'],
            company = company_object,
        )
        product.save()
    
    def update(self, custom_id):
        data = self.cleaned_data
        company_object = Suplier.objects.get(name=data['company'])
        Product.objects.filter(custom_id=custom_id).update(
            name = data['name'],
            number = data['number'],
            purchase = data['purchase'],
            selling = data['selling'],
            descriptions = data['descriptions'],
            company = company_object,
        )


class PurchaseOrderForm(forms.Form):
    CHOICE_STATUS = (
        (False, 'Not Delivered'),
        (True, 'Delivered')
    )
    status = forms.ChoiceField(
        label='Status',
        required=False,
        choices=CHOICE_STATUS,
        widget=forms.Select(
            attrs={
                'class': 'input-data',
                'required': True,
            }
        )
    )
    number = forms.CharField(
        label='Number',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-data',
                'required': True,
            }
        )
    )
    date = forms.DateField(
        label='Date',
        required=True,
        input_formats=['%d %B %Y'],
        widget=forms.TextInput(
            attrs={
                'class': 'datepicker-here input-data',
                'autocomplete': 'off',
                'required': True,
            }
        )
    )
    CHOICE = tuple(
        (idx['name'], idx['name']) for idx in Suplier.objects.values('name')
    )
    CHOICE_COMPANY = (('', ''),) + CHOICE
    company = forms.CharField(
        label='Company',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-data',
                'required': True,
            }
        )
    )
    name = forms.CharField(
        label='Name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-data',
                'required': True,
            }
        )
    )
    address = forms.CharField(
        label='Address',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-data',
                'required': True,
            }
        )
    )
    note = forms.CharField(
        label='Note',
        required=False,
        widget=CKEditorWidget(
            config_name='no_toolbar'
        )
    )

    def create(self, type_doc):
        data = self.cleaned_data
        company_object = Suplier.objects.get(name=data['company'])
        purchase_order = PurchaseOrder(
            status = data['status'],
            doc_type = type_doc,
            number = data['number'],
            date = data['date'],
            company = company_object,
            name = data['name'],
            address = data['address'],
            note = data['note']
        )
        purchase_order.save()

    def update(self, custom_id):
        data = self.cleaned_data
        company_object = Suplier.objects.get(name=data['company'])
        PurchaseOrder.objects.filter(custom_id=custom_id).update(
            status = data['status'],
            number = data['number'],
            date = data['date'],
            company = company_object,
            name = data['name'],
            address = data['address'],
            note = data['note']
        )


class OrderForm(forms.Form):
    product = forms.CharField(
        label='Product Name',
        widget=forms.TextInput(
            attrs={
                'class': 'table-input input-product',
                'placeholder': 'Product name',
                'required': True,
            }
        )
    )
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(
            attrs={
            'class': 'table-input input-quantity',
            'placeholder': 'Qty',
            'required': True,
            }
        )
    )

    def create(self, number):
        data = self.cleaned_data
        print(number)
        number_object = PurchaseOrder.objects.get(number=number)
        product_object = Product.objects.get(name=data['product'])
        order = Order(
            number = number_object,
            product = product_object,
            quantity = data['quantity']
        )
        order.save()