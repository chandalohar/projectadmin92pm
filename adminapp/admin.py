from django.contrib import admin
from.models import Contact,Carrers
class Contactadmin(admin.ModelAdmin):
    list_display = ['firstname','email','message','time','mobno']
    list_filter = ['time']
    class Meta:
        model = Contact
class Carrersadmin(admin.ModelAdmin):
    list_display = ['job_title','req_skills','contact_no','updated_time','job_location']
    list_filter = ['job_title','updated_time','job_location']
    class Meta:
        model = Carrers
admin.site.register(Contact,Contactadmin)
admin.site.register(Carrers,Carrersadmin)




