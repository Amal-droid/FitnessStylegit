from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from FSapp import *
from FSapp.forms import *
from FSapp.models import diet, Attendance


def customerashboard(request):
    return render(request, 'customer/customer_dashboard.html')


def allotedbatchdetails(request):
    data = Batch.objects.all()
    return render(request, 'customer/AllotedBatchDetails.html', {'data': data})


def viewdiet(request):
    data = diet.objects.all()
    return render(request, 'customer/view_diet.html', {'data': data})



def boookappoinments(request):
    appoinmentform = appoinment_form()
    if request.method == 'POST':
        appoinmentform= appoinment_form(request.POST)
        if appoinmentform.is_valid():
            appoinmentform.save()
            messages.info(request,"appoinment booked")
    return render(request,'customer/take_appointments.html',{'appoinmentform':appoinmentform})

def viewgymequipments(request):
    data = equipments.objects.all()
    return render(request,'customer/view_gym_equips.html',{'data':data})

def askmedicaldoubts(request):
    medicaldoubtsform =askmedicaldoubts_form()

    if request.method=='POST':
        medicaldoubtsform = askmedicaldoubts_form(request.POST)
        if medicaldoubtsform.is_valid():
            medicaldoubtsform.save()
            messages.info(request,'your doubts are added')
    return render(request,'customer/ask_medical_doubts.html',{'medicaldoubtsform':medicaldoubtsform})


def registercomplaints(request):
    complaints_form = complaint_form()
    if request.method=='POST':
        complaints_form=complaint_form(request.POST)
        if complaints_form.is_valid():
            complaints_form.save()
            messages.info(request, 'your complaints are added')
    return render(request,'customer/register_complaints.html',{'complaints_form':complaints_form})


def viewattendance(request):
    data = Attendance.objects.all()
    return render(request,'customer/view_attendance.html',{'data':data})


def viewbill(request):
    data = Bill.objects.all()
    return render(request,'customer/view_bill.html',{'data':data})
