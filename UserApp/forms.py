from django import forms
from django.contrib.auth.models import User
from UserApp.models import *

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )

class SignupForm(forms.Form):
    image_profile = forms.ImageField(
        label='Choose Your Profile',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'input-image',
                'accept': 'image/*',
            }
        )
    )
    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(
            attrs={
            'class': 'input-normal',
            }
        )
    )
    last_name = forms.CharField(
        label='Last Name',
        required=False,
        widget=forms.TextInput(
            attrs={
            'class': 'input-normal',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    retype_password = forms.CharField(
        label='Retype Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    birth_date = forms.DateField(
        label='Birth Date',
        required=True,
        input_formats=['%d %B %Y'],
        widget=forms.TextInput(
            attrs={
                'class': 'datepicker-here input-normal',
                'max': '01/01/2010',
                'min': '17/08/1945',
                'autocomplete': 'off'
            }
        )
    )
    birth_place = forms.CharField(
        label='Birth Place',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
                'autocomplete': 'off'
            }
        )
    )
    id_number = forms.CharField(
        label='ID',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    CHOICE_GENDER = (
        ('', 'Choose your gender'),
        ('ma', 'Male'),
        ('fe', 'Female')
    )
    gender = forms.ChoiceField(
        label='Gender',
        required=True,
        choices=CHOICE_GENDER,
        widget=forms.Select(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    address = forms.CharField(
        label='Address',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'input-normal input-long',
                'cols': '',
                'rows': '',
            }
        )
    )
    religion = forms.CharField(
        label='Religion',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    position = forms.CharField(
        label='Position',
        required=True,
        widget=forms.TextInput(
            attrs={
            'class': 'input-normal',
            }
        )
    )

    def create(self):
        data = self.cleaned_data
        username = data['email'].split('@')[0]
        new_user = User.objects.create_user(
            username = username.lower(),
            email = data['email'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            password = data['password']
        )
        new_user.save()
        new_biouser = BioUser(
            birth_date = data['birth_date'],
            birth_place = data['birth_place'],
            id_number = data['id_number'],
            gender = data['gender'],
            address = data['address'],
            religion = data['religion'],
            position = data['position'],
            user = new_user
        )
        new_biouser.save()

    def update_photo_profile(self, user, update_value):
        biodata = BioUser.objects.get(user=user)
        biodata.image_profile = update_value
        biodata.save()

    def update_biodata_user(self, user, update_key, update_value):
        bio_user = BioUser.objects.get(user=user)
        if update_key == 'email':
            user.email = update_value
            user.save()
        else:
            if update_key == 'birth_place':
                bio_user.birth_place = update_value
            elif update_key == 'birth_date':
                bio_user.birth_date = update_value
            elif update_key == 'religion':
                bio_user.religion = update_value
            elif update_key == 'position':
                bio_user.position = update_value
            elif update_key == 'address':
                bio_user.address = update_value
            bio_user.save()

    def change_class_input(self, class_name):
        for field in self.fields.keys():
            if field == 'birth_date':
                self.fields[field].widget.attrs['class'] = f'{class_name} datepicker-here'
            elif field == 'address':
                self.fields[field].widget.attrs['class'] = f'{class_name} input-long'
            elif field == 'image_profile':
                continue
            else:
                self.fields[field].widget.attrs['class'] = class_name


class SecretKeyForm(forms.Form):
    email = forms.EmailField(
        required=True,
        label='Email User',
        widget=forms.EmailInput(
            attrs={
                'class': 'input-normal',
            }
        )
    )
    user_key = forms.CharField(
        required=True,
        label='Secret Key',
        widget=forms.TextInput(
            attrs={
                'class': 'input-normal'
            }
        )
    )
    def save(self):
        data = self.cleaned_data
        user = User.objects.get(email=data['email'])
        user_key = data['user_key']
        if SecretKey.objects.filter(user=user).exists():
            SecretKey.objects.filter(user=user).update(
                secret_key = user_key,
            )
        else:
            secret_key = SecretKey(
                user=user,
                secret_key=user_key
            )
            secret_key.save()