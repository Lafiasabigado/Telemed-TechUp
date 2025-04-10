from django.contrib import admin
from core.models import User,Appointment,Feedback,MedicalRecord,Reminder

class UserAdmin(admin.ModelAdmin):
  list_display = ['username','email','is_patient','is_doctor']
admin.site.register(User,UserAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient",'doctor','datetime','status']
admin.site.register(Appointment,AppointmentAdmin)

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ["patient","created_at",'diagnosis','treatment','file']
admin.site.register(MedicalRecord,MedicalRecordAdmin)

class ReminderAdmin(admin.ModelAdmin):
    list_display = ["patient",'message','date_time']
admin.site.register(Reminder,ReminderAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["patient",'doctor','rating','comment']
admin.site.register(Feedback,FeedbackAdmin)