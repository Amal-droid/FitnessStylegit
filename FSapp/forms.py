from django import forms
from django.contrib.auth.forms import UserCreationForm

from FSapp.models import Login, Register_details, Batch, Instructor, equipments, Bill, health_details, appoinments, \
    medical_doubts, modelcomplaints, diet, Attendance


class DateInput(forms.DateInput):
    input_type = 'date'




class login_register(UserCreationForm):
    username = forms.CharField(label='username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

CHOICES = (
    ("M", "M"),
    ("F", "F")
)

class instructorsignupform(forms.ModelForm):
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Register_details
        fields = ["name", "DOB","gender", "age", "address", "mail", "phone", "qualification", "photo"]
        widgets = {
        'DOB' : DateInput()
        }


class usersignupform(forms.ModelForm):
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Register_details
        fields = ["name", "DOB", "gender", "age", "address", "mail", "phone", "photo", "consultation_time"]
        widgets = {
            'DOB': DateInput()
        }


class add_physicianform(forms.ModelForm):
    gender = forms.ChoiceField(choices = CHOICES, required=True, widget=forms.RadioSelect)

    class Meta:
        model = Register_details
        fields = ["name", "DOB", "gender", "age", "address", "mail", "phone", "photo", "qualification"]
        widgets = {
            'DOB': DateInput()
        }
class add_batch(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ["batch_name","batch_time","date"]

class add_instructor(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['batch','instructor']


class Gym_Equipments(forms.ModelForm):
        class Meta:
            model = equipments
            fields = ["equipments","equip_count","equip_weight"]

class billing(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['from_date','to_date','present_days','due_date']
        widgets ={
        'from_date' : DateInput(),
        'to_date': DateInput(),
        'due_date': DateInput()
        }


class viewbill(forms.ModelForm):
    class Meta:
        model = Bill
        fields =['user','amount','paid_on','bill_status']

         #
        #
        #
        # Physican Forms
        #
        #
        #
class add_health_details(forms.ModelForm):
    class Meta:
        model = health_details
        fields =['name','Height','Weight','transformation_status','medicine_consumption','health_issues']

class add_medicine_details(forms.ModelForm):
    class Meta:
        model = health_details
        fields =['name','Height','Weight','transformation_status','medicine_consumption','health_issues']

class appoinment_form(forms.ModelForm):
    class Meta:
        model = appoinments
        fields = ['name', 'physician', 'date']


class add_diet_form(forms.ModelForm):
    class Meta:
        model = diet
        fields =['day','food','time']



# customer


class askmedicaldoubts_form(forms.ModelForm):
    class Meta:
        model = medical_doubts
        fields = ['name','doubts']

class complaint_form(forms.ModelForm):
    class Meta:
        model =modelcomplaints
        fields = ['name','complaints']

