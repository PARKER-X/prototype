from django.shortcuts import render
from .models import *
from django.views.generic import CreateView
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.views.generic import ListView


# Create your views here.
# def appoinment(request):
#     return render(request, 'appoinment/appoinment.html')



class AppoinmentCreateView(CreateView):
    model = Patient
    fields = "__all__"
    template_name = "appoinment/appoinment.html"
    
# Render Pdf for meetup

def appoinment_render_pdf_view(request, *args, **kwargs):
    pk  = kwargs.get('pk')
    appoinment = get_object_or_404(Patient, pk=pk)
    user = request.user



    template_path = 'appoinment/pdf2.html'
    context = {'appoinment': appoinment, 'user':user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if download:
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
   #  response['Content-Disposition'] =  'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
