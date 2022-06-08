from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from UserApp.forms import *
from UserApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from WarehouseApp.app_func import *

# Create your views here.


@login_required(redirect_field_name='')
@user_passes_test(checkAdmin, redirect_field_name='')
def manage_user(request):
    user_list = BioUser.objects.all()
    table_header = {
        'display_only': ['Name'],
        'not_display_only': ['Email', 'Position'],
    }
    nav_active = {
        'users': 'active',
    }
    biouser = BioUser.objects.get(user=request.user)
    context = {
        'title': 'List User',
        'menu_active': nav_active,
        'user_list': user_list,
        'table_header': table_header,
        'biouser': biouser,
    }
    return render(request, 'datatable/all_user.html', context)


@login_required(redirect_field_name='')
def user_profile(request):
    user = request.user
    biouser = BioUser.objects.get(user=user)
    # print(biouser.has_image_profile)
    id_user = biouser.id_number
    data_user = {
        'email': user.email,
        'birth_place': biouser.birth_place,
        'birth_date': biouser.birth_date.strftime('%d %B %Y'),
        'religion': biouser.religion,
        'position': biouser.position,
        'address': biouser.address
    }
    biodata_form = SignupForm(initial=data_user)
    # Change Class Input
    biodata_form.change_class_input("input-profile")
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        user = authenticate(
            request, username=request.user.username, password=current_password)
        if user is not None:
            user.set_password(new_password)
            user.save()
            messages.success(
                request, 'Your password has been successfully updated')
            # If password changes, automatically redirect to login page
        else:
            messages.error(
                request, 'The password you entered is incorrect, check carefully the password you entered')
            return redirect('userapp:user-profile')
    context = {
        'title': 'User Profile',
        'biodata_form': biodata_form,
        'id_user': id_user,
        'biouser': biouser,
    }
    return render(request, 'profile.html', context)


@login_required(redirect_field_name='')
def update_user(request):
    bio_form = SignupForm()
    if request.is_ajax and request.method == 'POST':
        if request.FILES:
            value = request.FILES.get('image_profile')
            bio_form.update_photo_profile(request.user, value)
            return JsonResponse({}, status=200)
        else:
            key = list(request.POST.keys())[1]
            value = request.POST.get(key)
            bio_form.update_biodata_user(
                user=request.user, update_key=key, update_value=value)
            return JsonResponse({}, status=200)


@login_required(redirect_field_name='')
@user_passes_test(checkAdmin, redirect_field_name='')
def delete_user(request, user_id):
    user_id = user_id.split("+")
    for one_id in user_id:
        one_id = int(one_id)
        user = User.objects.get(id=one_id)
        user.delete()
    return redirect('userapp:accessibility')


def login_view(request):
    if request.method == 'POST':
        try:
            email_user = request.POST.get('email').lower()
            password_user = request.POST.get('password')
            username_user = User.objects.get(email=email_user).username
            user = authenticate(
                request, username=username_user, password=password_user)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(
                    request, 'The email or password you entered is wrong')
        except:
            messages.error(
                request, 'The email or password you entered is wrong')
    login_form = LoginForm()
    context = {
        'title': 'Login',
        'login_form': login_form,
        'login_or_signup': True,
    }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST or None)
        if signup_form.is_valid():
            signup_form.create()
            fullname = request.POST.get(
                'first_name') + ' ' + request.POST.get('last_name')
            email = request.POST.get('email')
            content = f'Terdapat User baru dengan\nNama:{fullname}\nEmail:{email}'
            send_text_email('Ada User Baru', content,
                            ['devkillua33@gmail.com'])
            return redirect('userapp:login')
        else:
            messages.error(
                request, 'the data failed to create please check again, make sure there are no errors')
    signup_form = SignupForm()
    context = {
        'title': 'Signup',
        'signup_form': signup_form,
        'login_or_signup': True,
    }
    return render(request, 'signup.html', context)


def change_password(request):
    user_key = request.GET.get('user_key')
    if SecretKey.objects.filter(secret_key=user_key).exists():
        secret_key = SecretKey.objects.get(secret_key=user_key)
        user = User.objects.get(username=secret_key.user.username)
        if request.method == 'POST':
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            secret_key.delete()
            return redirect('userapp:login')
        pass_form = SignupForm()
        context = {
            'title': 'New Password',
            'is_user': True,
            'pass_form': pass_form,
        }
        return render(request, 'change_pass.html', context)
    else:
        context = {
            'title': 'Broken Link',
            'is_user': False
        }
        return render(request, 'change_pass.html', context)


def sending_reset(request):
    context = {
        'title': 'Reset Password',
        'email_sending': True,
    }
    return render(request, 'forgot_pass.html', context)


def forgot_password(request):
    if request.method == 'POST':
        email_user = request.POST.get('email')
        if User.objects.filter(email=email_user).exists():
            secret_reset = uniqueString(50)
            while SecretKey.objects.filter(secret_key=secret_reset).exists():
                secret_reset = uniqueString(50)
            secret_form = SecretKeyForm(
                {'email': email_user, 'user_key': secret_reset})
            if secret_form.is_valid():
                secret_form.save()
            domain = request.META['HTTP_ORIGIN']
            path = reverse('userapp:change-password')
            full_url = domain + path + '?' + f'user_key={secret_reset}'
            content = {'link': full_url}
            send_html_email('Reset Password', content, [
                            email_user], 'send_email/reset_password.html')
            return redirect('userapp:sending-reset')
        else:
            messages.error(
                request, "The email you entered is not in our system")
    pass_form = SignupForm()
    context = {
        'title': 'Reset Password',
        'pass_form': pass_form,
        'email_sending': False,
    }
    return render(request, 'forgot_pass.html', context)


def logout_view(request):
    logout(request)
    return redirect('userapp:login')
