import random
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


"""
uniqueString Return String Random
Parameter = length(int)[required]
            string(str)
Default = string : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
"""
characters_default = list(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def uniqueString(length, characters=characters_default):
    unique = ""
    for i in range(length):
        random.shuffle(characters)
        unique += random.choice(characters)
    return unique


def checkAdmin(user):
    if user.is_superuser:
        return True
    else:
        return False


def send_html_email(subject, content, email_to, template):
    from_email = settings.EMAIL_HOST_USER
    email_to = [email_to] if type(email_to) == str else email_to
    html_content = render_to_string(
        template,
        {
            'title': subject,
            'content': content,
        }
    )
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, email_to)
    email.attach_alternative(html_content, 'text/html')
    email.send()


def send_text_email(subject, content, email_to):
    from_email = settings.EMAIL_HOST_USER
    email_to = [email_to] if type(email_to) == str else email_to
    send_mail(subject, content, from_email, email_to)
