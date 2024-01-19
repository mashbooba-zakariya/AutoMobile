from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from AutoMobileApp.forms import CustomerRegister, LoginRegister, ManagerRegister, ScheduleForm, FeedbackForm, \
    FeedbackReplyForm
from AutoMobileApp.models import Customer, Manager, Feedback, Appointment, Schedules, Login


# Create your views here.
def index(request):
    return render(request,'index.html')


def base(request):
    return render(request,'base.html')



#----------Customer Registration form function------------
def Customer_Register(request):
    login_register = LoginRegister()
    customer_register = CustomerRegister()


    if request.method == 'POST':
        user1 = LoginRegister(request.POST)
        user2 = CustomerRegister(request.POST)

        if user1.is_valid() and user2.is_valid():
            form = user1.save(commit = False)
            form.is_customer = True
            form.save()

            data = user2.save(commit = False)
            data.user = form
            data.save()

            return redirect('login_form')
    return render(request, 'CustomerReg.html',{'customer_register':customer_register,'login_register':login_register})


#----------Work Manager Registration form function-----------
def Manager_Register(request):
    login_register = LoginRegister()
    manager_register = ManagerRegister()


    if request.method == 'POST':
        user1 = LoginRegister(request.POST)
        user2 = ManagerRegister(request.POST)

        if user1.is_valid() and user2.is_valid():
            form = user1.save(commit=False)
            form.is_manager = True
            form.save()

            data = user2.save(commit=False)
            data.user = form
            data.save()

            return redirect('login_form')
    return render(request,'ManagerReg.html',{'login_register':login_register,'manager_register':manager_register})


#--------Login form function--------
def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_base')
            elif user.is_customer:
                return redirect('customer_base')
            elif user.is_manager:
                return redirect('manager_base')

        else:
            messages.info(request,"User not found")

    return render(request,'login_form.html')



#----------admin Dashboard function----------
def admin_base(request):
    return render(request,'adminDashboard/admin_base.html')


#----------customer Dashboard function----------
def customer_base(request):
    return render(request,'customerDashboard/customer_base.html')


#-------manager Dashboard function-----------
def manager_base(request):
    return render(request,'managerDashboard/manager_base.html')


#------Admin can View the Customer function----------
def AdminCustomerView(request):
    data = Customer.objects.all()
    return render(request,'adminDashboard/AdminCustomer.html',{'data':data})


#----------- Admin Can delete the customer----------
def AdminCustomerDelete(request,id):
    if request.method == 'POST':
        data_id = Customer.objects.get(id=id)
        data_id.delete()
        return redirect('AdminCustomerView')

#------------Admin can view the manager----------
def AdminManagerView(request):
    data = Manager.objects.all()
    return render(request,'adminDashboard/AdminManager.html',{'data':data})


#--------Admin can Update the details of manager
def AdminManagerUpdate(request):
    data = Manager.objects.get(id=id)
    updated_data = ManagerRegister(instance=data)

    if request.method == 'POST':
        updated_data = ManagerRegister(request.POST,instance=data)
        if updated_data.is_valid():
            updated_data.save()
            return redirect('AdminManagerView')
    return render(request,'adminDashboard/AdminManagerUpdate.html',{'updated_data':updated_data})


#---------Admin can delete the manager---------
def AdminManagerDelete(request,id):
    if request.method == 'POST':
        data_id = Manager.objects.get(id=id)
        data_id.delete()
        return redirect('AdminManagerView')


#--------------- SLot Scheduling By Admin---------------
def SlotSchedule(request):
    form = ScheduleForm

    if request.method == 'POST':
        form =ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_base')

    return render(request,'adminDashboard/SlotSchedule.html',{'form':form})


# --------Slot view from Customer---------

def SlotView(request):
    slot = Schedules.objects.all()
    return render(request,'customerDashboard/SlotView.html',{'slot':slot})





# -----------Booking Slot from Customer----------

def SlotBooking(request,id):
    schedule = Schedules.objects.get(id=id)
    user = request.user
    print(user)
    use = Customer.objects.get(user = user)
    print(use)
    print(schedule)
    appointment = Appointment.objects.filter(user=use, Slots=schedule)
    if appointment.exists():
        messages.info(request,'You already request for the appointment for this schedule')
        return redirect('customer_base')
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = use
            obj.schedule = schedule
            obj.save()
            messages.info(request,'Appointment Booked successfully')
            return redirect('customer_base')
        return render(request,'customerDashboard/SlotBooking.html',{'schedule':schedule})



def Appointments(request):
    user = Customer.objects.get(user = request.user)
    appointment = Appointment.objects.filter(user=user)
    return render(request,'customerDashboard/Appointments.html',{'appointment':appointment})








#---------Feedback from the customer----------
def CustomerFeedback(request):
    data = FeedbackForm
    user = request.user
    if request.method == 'POST':
        data = FeedbackForm(request.POST)
        if data.is_valid():
            obj = data.save(commit=False)
            obj.user = user
            obj.save()
            return redirect('customer_base')
    return render(request,'customerDashboard/Feedback.html',{'data':data})


#--------Feedback Reply from Admin---------
def AdminFeedbackReply(request,):
    data = Feedback.objects.all()
    return render (request,'adminDashboard/FeedbackReply.html',{'data':data})


def AdminFeedReply(request,id):
    data = Feedback.objects.get(id=id)
    form = FeedbackReplyForm(instance=data)

    if request.method == 'POST':
        form = FeedbackReplyForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('AdminFeedbackReply')

    return render(request,'adminDashboard/Reply.html',{'form':form})



def CustomerFeedbackView(request):
    user1 = request.user
    data = Feedback.objects.filter(user=user1)
    return render(request,'customerDashboard/CustomerFeedbackView.html',{'data':data})