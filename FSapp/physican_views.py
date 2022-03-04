from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from FSapp import *
from FSapp.forms import *
from FSapp.models import first_aid, appoinments, medical_doubts


def physiciandashboard(request):
    return render(request,'physican/physician_dashboard.html')


def addhealthdetails(request):
    form = add_health_details()
    if request.method == 'POST':
        form = add_health_details(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "added")
            return redirect("Addhealthdetails")
        else:
            form = add_health_details()
    return render(request,'physican/add_health_details.html',{'form':form})

def addMedicine(request):
    form = add_medicine_details()
    if request.method == 'POST':
        form = add_medicine_details(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "added")
            return redirect("Addmedicine")
        else:
            form = add_medicine_details()
    return render(request, 'physican/add_Medicine.html', {'form': form})


def updatehealthdetailspage(request):
    data = health_details.objects.all()

    return render(request,'physican/Update_health_details.html',{'data':data})



def updatemedicinedetailspage(request):
    data = health_details.objects.all()
    return render(request,'physican/Update_medicine_details.html',{'data': data})


def firstaid(request):
    data = first_aid.objects.all()
    return render(request,'physican/view_first_aid.html')



def updateHbutton(request,id):
    data = health_details.objects.get(id=id)
    form = add_health_details(instance=data )
    if request.method == 'POST':
        form = add_health_details(request.POST,instance = data)
        if form.is_valid():
            form.save()
            return redirect('UpdateHealthDetails')

    return render(request,'physican/UpdateH_Form.html',{'form':form})


def updateUbutton(request,id):
    data = health_details.objects.get(id = id)
    form = add_medicine_details(instance = data)
    if request.method == 'POST':
        form = add_medicine_details(request.post,instance=data)
        if form.is_valid():
            form.save()
            return redirect('UpdateMedicineDetails')

    return render(request,'physican/updateU_Form.html',{'form': form})

def viewappoinments(request):
    data = appoinments.objects.all()
    return render(request,'physican/view_appoinments.html',{'data': data})

def approve(request,id):
    data = appoinments.objects.get(id=id)
    data.approval_status = 1
    data.save()
    return redirect('ViewAppoinments')


def reject(request,id):
    data = appoinments.objects.get(id=id)
    data.approval_status = 2
    data.save()
    return redirect('ViewAppoinments')

def medicaldoubts(request):
    data = medical_doubts.objects.all()
    return render(request,'physican/view_medicaldoubts.html',{'data':data})