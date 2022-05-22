from django.urls import path, re_path
from UserApp import views

app_name = 'UserApp'
urlpatterns = [
    # Invoice And PO URL
    path('profile', views.user_profile, name='user-profile'),
    path('accessibility', views.manage_user, name='accessibility'),
    re_path(r'^delete_id=(?P<user_id>[\d\+]+)$', views.delete_user, name='delete-user'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('password', views.change_password, name='change-password'),   
    path('password/reset', views.forgot_password, name='reset-password'),
    path('password/reset/confirm', views.sending_reset, name='sending-reset'),
    path('post/ajax/user', views.update_user, name='user-update')
]
# 
