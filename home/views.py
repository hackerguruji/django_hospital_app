from django.shortcuts import render
from home.models import Form
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Home page")

def consultation(request):
        
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            age = request.POST.get('age')
            work = request.POST.get('work')
            worktype = request.POST.get('worktype')
            pain = request.POST.get('pain')
            bleeding = request.POST.get('bleeding')
            burning = request.POST.get('burning')
            itching = request.POST.get('itching')
            constipation = request.POST.get('constipation')
            discharge = request.POST.get('discharge')
            prolepse = request.POST.get('prolepse')
            anus = request.POST.get('anus')
            othercom = request.POST.get('othercom')
            familyten = request.POST.get('familyten')
            consultation = Form(name=name, address=address , phone=phone, age=age, 
            work=work, worktype=worktype, pain=pain, bleeding=bleeding, burning=burning, itching=itching, constipation=constipation, 
            discharge=discharge, prolepse=prolepse, anus=anus, othercom=othercom, familyten=familyten,)
            
            consultation.save()
    
            messages.success(request, 'Your message has been sent !')

        
        return render(request, 'consultation.html')


def report(request):
    data= Form.objects.all()
    return render(request, 'report.html' ,{"mess":data} )
   

