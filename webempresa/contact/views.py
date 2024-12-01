from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ReservationForm
from webempresa.settings import EMAIL_HOST_USER

def reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            number_of_people = form.cleaned_data['number_of_people']

            email_message = EmailMessage(
                subject="Nueva reserva en el restaurante",
                body=f"Reserva de mesa para {name} <{email}>\n\nDetalles:\nFecha: {date}\nHora: {time}\nNúmero de personas: {number_of_people}",
                from_email=EMAIL_HOST_USER,
                to=["63f6f681b3d1ef@inbox.mailtrap.io"],
                reply_to=[email]
            )

            try:
                email_message.send()
                return redirect(reverse('reservation') + "?ok")
            except:
                return redirect(reverse('reservation') + "?fail")
    else:
        form = ReservationForm()

    return render(request, "contact/reservation.html", {"form": form})

