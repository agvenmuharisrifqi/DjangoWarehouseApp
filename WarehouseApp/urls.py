from django.contrib import admin
from django.urls import path, include
from WarehouseApp.views import index, error, new_user
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404

handler400 = 'WarehouseApp.views.error_handler'
handler403 = 'WarehouseApp.views.error_handler'
handler404 = 'WarehouseApp.views.error_handler'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('ProductApp.urls', namespace='productapp')),
    path('user/', include('UserApp.urls', namespace='userapp')),
    path('', index, name='index'),
    path('404', error, name='error'),
    path('new-user', new_user, name='new-user')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
