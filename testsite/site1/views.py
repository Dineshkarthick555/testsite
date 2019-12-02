from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def testex(request):
    try:
        data=Employee.object.get(id=12)
    except NameError:
        return HttpResponse("No Records found for Employee")
    return HttpResponse(data)
    
#Session
def setsession(request):
    request.session['username']='Karthik'
    request.session['password']='1234567890'
    return HttpResponse("Session set")
def getsession(request):
    username=request.session['username']
    password=request.session['password']
    return HttpResponse(username+" "+password)
  
#Cookies 
def setcookie(request):
    response=HttpResponse("Cookie set")
    response.set_cookie('cool','Karthik')
    return response
def getcookie(request):
    name=request.COOKIES['cool']   
    return HttpResponse(name)

#CSV File
import csv
def getfile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="file.csv"'
    writer=csv.writer(response)
    writer.writerow(['Hi','Hello','1','2','3'])
    writer.writerow(['Welcome','Python','4','5','6'])
    return responses

#CSV from database
from site1.models import Pytest
def getfiledb(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment:filename="myfile.csv"'
    pytest=Pytest.objects.all()
    writer=csv.writer(response)
    for pyt in pytest:
        writer.writerow([pyt.id,pyt.firstname,pyt.lastname,pyt.email,pyt.age])
    return response
        
#Creating PDF File
from reportlab.pdfgen import canvas
def getpdf(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="myfile.pdf"'
    p=canvas.Canvas(response)
    p.setFont("Times-Roman",30)
    p.drawString(100,700,"Hello Karthik")
    p.showPage()
    p.save()
    return response
 
from django.template import loader
def index(request):
    return render(request,'index.html')