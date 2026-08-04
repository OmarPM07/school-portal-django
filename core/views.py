from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import PaginaInstitucional
from .forms import ContactoForm
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def pagina_institucional(request, slug):
    pagina = get_object_or_404(PaginaInstitucional, slug=slug, activo=True)
    return render(request, 'core/pagina_institucional.html', {'pagina': pagina})

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            cuerpo_correo = f"Mensaje de: {nombre} ({email})\n\n{mensaje}"

            try:
                send_mail(
                    subject=f"[Contacto CBTA 108] {asunto}",
                    message=cuerpo_correo,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.CONTACT_EMAIL_RECEIVER],
                    fail_silently=False,
                )
                messages.success(request, "Tu mensaje fue enviado correctamente. Te responderemos pronto.")
            except Exception:
                messages.error(request, "Ocurrió un error al enviar tu mensaje. Intenta de nuevo más tarde.")

            form = ContactoForm()  # limpiar formulario tras envío exitoso
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form})