from django.urls import path, re_path
from ProductApp import views

app_name = 'ProductApp'
urlpatterns = [
    # Invoice And PO URL
    path('doc/all', views.all_doc, name='all-doc'),
    path('doc/add', views.add_doc, name='add-doc'),
    path('doc/edit', views.edit_doc, name='edit-doc'),
    path('doc/delete', views.del_doc, name='del-doc'),
    # Product URL
    path('product/all', views.all_product, name='all-product'),
    path('product/add', views.add_product, name='add-product'),
    re_path(r'^product/edit_id=(?P<product_id>\w+)$', views.edit_product, name='edit-product'),
    re_path(r'^product/delete_id=(?P<product_id>[\d\+]+)$', views.del_product, name='delete-product'),
    # Suplier URL
    path('suplier/all', views.all_suplier, name='all-suplier'),
    path('suplier/add', views.add_suplier, name='add-suplier'),
    re_path(r'^suplier/edit_id=(?P<suplier_id>\w+)$', views.edit_suplier, name='edit-suplier'),
    re_path(r'^suplier/delete_id=(?P<suplier_id>[\d\+]+)$', views.del_suplier, name='delete-suplier'),
    #Ajax
    path('get/ajax', views.get_data, name='get-data'),
    path('print/', views.single_doc, name='single-doc'),
]
# 
