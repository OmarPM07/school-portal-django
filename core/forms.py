# core/forms.py

from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo electrónico'})
    )
    asunto = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto'})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Escribe tu mensaje'})
    )

    # Honeypot anti-spam: campo oculto que los bots suelen llenar, pero los humanos no ven ni llenan
    telefono_confirmacion = forms.CharField(required=False, widget=forms.HiddenInput())

    def clean_telefono_confirmacion(self):
        valor = self.cleaned_data.get('telefono_confirmacion')
        if valor:
            raise forms.ValidationError("Spam detectado.")
        return valor