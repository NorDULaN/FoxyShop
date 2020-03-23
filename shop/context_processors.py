from .models import Brand, Rubric
from .forms import MailingForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

def brand(request):
    brands = Brand.objects.all()
    return {'brands': brands}

def rubric(request):
    rubrics = Rubric.objects.all()
    return {'rubrics': rubrics}

def favourite(request):
    if request.user.is_authenticated:
        user = request.user
        favourite = user.favourite.all()
    else:
        user = None
        favourite = None
    return {'favourite': favourite}

def mailing(request):
    if request.method == 'POST' and 'mailing_form' in request.POST:
        mailing_form = MailingForm(request.POST)
        if mailing_form.is_valid():
            cd = mailing_form.cleaned_data
            subject = 'Рассылка FoxyShop'
            message = 'Подписка на рассылку прошла успешно!'
            msg_html = render_to_string('email.html', {})
            send_mail(subject, message, 'FoxyShop',[cd['mailing_email']],  html_message=msg_html)
            post = True
            return {'mailing_form': mailing_form, 'post': post}
    else:
        mailing_form = MailingForm()
        post = False
        return {'mailing_form': mailing_form, 'post': post}
