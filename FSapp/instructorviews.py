from django.contrib import messages
from django.shortcuts import render, redirect
from FSapp.forms import *
from FSapp.models import *


def instructordashboard(request):
    return render(request, 'instructor/instructor_dashboard.html')


def addUserHealthDetails(request):
    form = add_health_details()
    if request.method == 'POST':
        form = add_health_details(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'instructor/add_update_customer_health_details.html', {'form': form})


def viewUserHealthDetails(request):
    data = health_details.objects.all()
    return render(request, 'instructor/update_customer_health_details.html', {'data': data})


def Updateuserhealthdetails(request, id):
    data = health_details.objects.get(id=id)
    if request.method == 'POST':
        form = add_health_details(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('updateuserhealthdetails')
    else:
        form = add_health_details(instance=data)
    return render(request, 'instructor/add_update_customer_health_details.html', {"form": form})



def adduserdiet(request):
    form = add_diet_form()
    if request.method == 'POST':
        form = add_diet_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = add_diet_form()
    return render(request, 'instructor/add_update_diet.html',{"form":form})


def viewUserdiet(request):
    data = diet.objects.all()
    return render(request, 'instructor/view_update_user_diet.html', {'data': data})


def Updateuserdiet(request,id):
    data = diet.objects.get(id=id)
    if request.method == 'POST':
        form = add_diet_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewuserdiet')
    else:
        form = add_diet_form(instance=data)
    return render(request, 'instructor/add_update_diet.html', {"form": form})

def add_equipments(request):
    if request.method == 'POST':
        form = Gym_Equipments(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"data added")
        return redirect('add_gym_equipments')
    else:
        form = Gym_Equipments()
    return render(request,'instructor/add_gym_equip.html',{'form':form})

def attendance(request):
    
    return render(request,'instructor/add_user_attendance.html',{})