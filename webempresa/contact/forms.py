from django import forms

class ReservationForm(forms.Form):
    name = forms.CharField(
        label='Nombre',
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        min_length=3,
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Escribe tu email', 'class': 'form-control'})
    )
    date = forms.DateField(
        label='Fecha de la reserva',
        required=True,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    time = forms.TimeField(
        label='Hora de la reserva',
        required=True,
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'})
    )
    number_of_people = forms.IntegerField(
        label='Número de personas',
        min_value=1,
        max_value=20,  # puedes ajustar el límite según lo que permita tu restaurante
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Número de personas', 'class': 'form-control'})
    )

