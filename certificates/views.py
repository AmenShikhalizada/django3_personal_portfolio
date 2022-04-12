from django.shortcuts import get_object_or_404, render
from .models import Certificate

def all_certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'certificates/certificates.html', {'certificates': certificates})


def detail(request, certificate_id):
    certificates = get_object_or_404(Certificate, pk=certificate_id)
    return render(request, 'certificates/detail.html', {'certificates':certificates})

