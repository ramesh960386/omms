from django.contrib import admin
from app32.models import EmpModel, RoleModel, DeptModel, RoomModel, FacilityModel


class EmpAdmin(admin.ModelAdmin):
    #fields = ['Emp_ID', 'Phone_No']
    ordering = ['Emp_ID']
    search_fields = ['Emp_ID']
    list_filter = ['Emp_ID']
    list_display = ['Emp_ID', 'First_Name', 'Last_Name', 'Phone_No', 'Email_ID']
    list_editable = ['Email_ID']


class RoomAdmin(admin.ModelAdmin):
    ordering = ['RoomID']
    search_fields = ['Name']
    list_display = ['RoomID', 'Name', 'Facility']


admin.site.register(EmpModel, EmpAdmin)
admin.site.register(RoleModel)
admin.site.register(DeptModel)
admin.site.register(RoomModel, RoomAdmin)
admin.site.register(FacilityModel)
