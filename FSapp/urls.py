from django.urls import path

from FSapp import views, physican_views, customer_views, instructorviews
        
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_instructor/', views.addinstructor, name='add_instructor'),
    path('add_physician/', views.add_physician, name='add_physician'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('add_batch/', views.addbatch, name='add_batch'),
    path('batch_details/', views.view_batches, name='batch_details'),
    path('view_attendance/', views.viewattendance, name='view_attendance'),
    path('add_gym_equip/', views.add_equipments, name='add_gym_equip'),
    path('remove_equips/', views.removegymequip, name='remove_equips'),
    path('delete/<int:id>',views.delete,name = 'delete'),
    path('generatebill/',views.billpage,name='generatebill'),
    path('generate/',views.generatebill,name='generate'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('viewcomplaints/',views.viewcomplaints,name ='viewcomplaints'),




    path('physician_dashboard/',physican_views.physiciandashboard,name='physician_dashboard'),
    path('Addhealthdetails/',physican_views.addhealthdetails,name='Addhealthdetails'),
    path('Addmedicine/',physican_views.addMedicine,name='Addmedicine'),
    path('UpdateHealthDetails',physican_views.updatehealthdetailspage,name='UpdateHealthDetails'),
    path('UpdateMedicineDetails/',physican_views.updatemedicinedetailspage,name='UpdateMedicineDetails'),
    path('Firstaid/',physican_views.firstaid,name='Firstaid'),
    path('addFirstaid/',physican_views.addfirstaid,name='addFirstaid'),
    path('UpdateH_Form/<int:id>/',physican_views.updateHbutton,name='UpdateH_Form'),
    path('updateU_Form/<int:id>/',physican_views.updateUbutton,name='updateU_Form'),
    path('ViewAppoinments/',physican_views.viewappoinments,name='ViewAppoinments'),
    path('approve/<int:id>/',physican_views.approve,name ='approve'),
    path('reject/<int:id>/',physican_views.reject,name ='reject'),
    path('medicalDoubts/',physican_views.medicaldoubts,name = 'medicalDoubts'),


    path('customerdashboard/',customer_views.customerashboard,name = 'customerdashboard'),
    path('allotedBatchDetails/',customer_views.allotedbatchdetails,name = 'allotedBatchDetails'),
    path('diet/',customer_views.viewdiet,name='diet'),
    path('bookappoinment/',customer_views.boookappoinments,name='bookappoinment'),
    path('viewgymequipments/',customer_views.viewgymequipments,name = 'viewgymequipments'),
    path('askmedicladoubts/',customer_views.askmedicaldoubts,name ='askmedicladoubts'),
    path('complaints_form/',customer_views.registercomplaints,name ='complaints_form'),
    path('viewattendance/',customer_views.viewattendance,name='viewattendance'),
    path('viewbill/',customer_views.viewbill,name = 'viewbill'),





    path('instructordashboard/',instructorviews.instructordashboard,name ='instructordashboard'),
    path('addupdateuserhealthdetails/',instructorviews.addUserHealthDetails,name = 'addUserHealthDetails'),
    path('updateuserhealthdetails/',instructorviews.viewUserHealthDetails,name ='updateuserhealthdetails'),
    path('Hupdatebutton/<int:id>/',instructorviews.Updateuserhealthdetails,name='Hupdatebutton'),
    path('adduserdiet/',instructorviews.adduserdiet,name ='adduserdiet'),
    path('viewuserdiet/',instructorviews.viewUserdiet,name='viewuserdiet'),
    path('udietbutton/<int:id>',instructorviews.Updateuserdiet,name ='udietbutton'),
    path('add_gym_equipments/',instructorviews.add_equipments,name ='add_gym_equipments'),
    path('addattendance/',instructorviews.attendance,name='addattendance')
]