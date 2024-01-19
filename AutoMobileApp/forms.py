import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import DateInput

from AutoMobileApp.models import Login, Customer, Manager, Schedules, Feedback


#------------- Form for Login Page------------
class LoginRegister(UserCreationForm):

    class Meta:
        model = Login
        fields = ('username','password1','password2')



#------------- Form for Customer register------------
class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user',)


#------------- Form for Manager register------------
class ManagerRegister(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'
        exclude = ('user',)



#-------Form for Schedule slot for booking---------
class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'


class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    Start_time = forms.TimeField(widget=TimeInput)
    end_time = forms.TimeField(widget=TimeInput)


    class Meta:
        model = Schedules
        fields = ('date','Start_time','end_time')


    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        Start_time = cleaned_data.get('Start_time')
        end_time = cleaned_data.get('end_time')

        if date <= datetime.date.today():
            raise forms.ValidationError("this date is past !!!")


        if Start_time >= end_time:
            raise forms.ValidationError("this time is not accepted !!!!")


        return cleaned_data








#------------- Form for feedback from customer------------

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('description',)


class FeedbackReplyForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('reply',)