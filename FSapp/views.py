from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from FSapp.forms import *
from FSapp.models import Attendance, equipments


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_home')
            if user.is_customer:
                return redirect('customerdashboard')
            if user.is_physician:
                return redirect('physician_dashboard')
        else:
            messages.info(request,"invalid credentials")
    return render(request,'login.html')

def admin_home(request):
    return render(request, 'admin_home.html')


def addinstructor(request):
    form = login_register()
    form2 = instructorsignupform()
    if request.method == 'POST':
        form2 = instructorsignupform(request.POST)
        form = login_register(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            user.is_physician = True
            user.save()
            a = form2.save(commit=False)
            a.user = user
            a.save
            messages.info(request,"instructor added")
            return redirect('add_instructor')
    return render(request,'add_instructor.html', {'form': form,'form2':form2})


def add_customer(request):
    form = login_register()
    form2 = usersignupform()
    if request.method == "POST":
        form = login_register(request.POST)
        form2 = usersignupform(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            user.is_customer =True
            user.save()
            a = form2.save(commit=False)
            a.user=user
            a.save
            messages.info(request,"USER ADDED")
    return render(request,'user_register.html',{'form': form,'form2':form2})




def add_physician(request):
    add_physicianform1 = add_physicianform()
    login_form = login_register()
    if request.method == 'POST':
        add_physicianform1 = add_physicianform(request.POST, request.FILES)
        login_form = login_register(request.POST)
        if login_form.is_valid() and add_physicianform1.is_valid():
            a=login_form.save(commit=False)
            a.is_physican=True
            a.save()
            physican = add_physicianform1.save(commit=False)
            physican.a = a
            physican.save()
            messages.info(request,"physician added")
            add_physicianform1.save()
    return render(request, 'add_physician.html',{'add_physicianform1': add_physicianform1,'login_form': login_form})




def view_staff(request):
    data = Register_details.objects.all()
    print(data)
    return render(request, 'view_staff.html', {'data': data})


def addbatch(request):
    if request.method == 'POST':
        form = add_batch(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"batch added")
            return redirect("add_batch")
    else:
        form = add_batch()
    return render(request, 'add_batch.html', {'form': form})





def view_batches(request):
    batch = Batch.objects.all()

    instructor = Instructor.objects.all()
    return render(request,'batch_details.html',{'batch' : batch, 'instructor' : instructor})


def viewattendance(request):
    attendance_details = Attendance.objects.all()
    return render(request,'view_attendance.html')


def add_equipments(request):
    if request.method == 'POST':
        form = Gym_Equipments(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"data added")
        return redirect('add_gym_equip')
    else:
        form = Gym_Equipments()
    return render(request,'add_equipments.html',{'form':form})

def removegymequip(request):
    items = equipments.objects.all()

    return render(request,'remove_equips.html',{'items':items,})

def delete(request,id):
    data = equipments.objects.get(id=id)
    data.delete()
    return redirect('remove_equips')


def billpage(request):
    form = billing
    if request.method == 'POST':
        form = billing(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"bill generated")
    return render(request,'generate_bill.html',{'form':form})
def generatebill(request):
    return  render(request,'generate_bill.html')

def viewfeedback(request):
    return render(request,'view_feedback.html')

def services(request):
    return render(request,'services.html')
# Create your views here.
