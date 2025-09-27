from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from weasyprint import HTML, CSS
from .models2 import FichaEstudiantil
import tempfile

def generar_pdf(request, ficha_id):
    ficha = get_object_or_404(FichaEstudiantil, pk=ficha_id)
    html_string = render(request, 'ficha_pdf.html', {'ficha': ficha}).content.decode('utf-8')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=ficha_{ficha.rut}.pdf'

    with tempfile.NamedTemporaryFile(delete=True) as temp:
        HTML(string=html_string).write_pdf(response, stylesheets=[CSS('static/css/pdf.css')])

    return response
