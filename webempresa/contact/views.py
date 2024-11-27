from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactForm
from webempresa.settings import EMAIL_HOST_USER

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']


            email_message = EmailMessage(
                subject="Nuevo mensaje de contacto",
                body=f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                from_email=EMAIL_HOST_USER,
                to=["63f6f681b3d1ef@inbox.mailtrap.io"],
                reply_to=[email]
            )

            try:
                email_message.send()
                return redirect(reverse('contact') + "?ok")
            except:
                return redirect(reverse('contact') + "?fail")
    else:
        form = ContactForm()

    return render(request, "contact/contact.html", {"form": form})
