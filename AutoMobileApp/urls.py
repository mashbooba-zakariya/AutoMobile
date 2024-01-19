from django.urls import path

from AutoMobileApp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('base',views.base,name='base'),
    path('CustomerRegister',views.Customer_Register,name='CustomerRegister'),
    path('ManagerRegister',views.Manager_Register,name='ManagerRegister'),
    path('login_form',views.login_form,name='login_form'),
    path('admin_base',views.admin_base,name='admin_base'),
    path('customer_base',views.customer_base,name='customer_base'),
    path('manager_base',views.manager_base,name='manager_base'),
    path('AdminCustomerView',views.AdminCustomerView,name='AdminCustomerView'),
    path('AdminCustomerDelete/<int:id>',views.AdminCustomerDelete,name='AdminCustomerDelete'),
    path('AdminManagerView',views.AdminManagerView,name='AdminManagerView'),
    path('AdminManagerUpdate/<int:id>',views.AdminManagerUpdate,name='AdminManagerUpdate'),
    path('AdminManagerDelete/<int:id>',views.AdminManagerDelete,name='AdminManagerDelete'),
    path('SlotSchedule',views.SlotSchedule,name='SlotSchedule'),
    path('CustomerFeedback',views.CustomerFeedback,name='CustomerFeedback'),
    path('AdminFeedbackReply',views.AdminFeedbackReply,name='AdminFeedbackReply'),
    path('AdminFeedReply/<int:id>',views.AdminFeedReply,name='AdminFeedReply'),
    path('CustomerFeedbackView',views.CustomerFeedbackView,name='CustomerFeedbackView'),
    path('SlotView',views.SlotView,name='SlotView'),
    path('Appointments',views.Appointments,name='Appointments'),
    path('SlotBooking/<int:id>/',views.SlotBooking,name='SlotBooking'),


]