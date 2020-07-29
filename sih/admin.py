from django.contrib import admin
from . import models
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import People


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = People
    list_display = ('EmailId','name','gender','Age','Aadhar_Number','ContactNumber','RecoveryMail','RecoveryNumber',
                    'Longitude','Latitude','City','Address','LocationDateTime','is_staff', 'is_active',)
    list_filter = ('EmailId', 'is_staff', 'is_active',)
    #Below fieldsets is for editing purposes
    fieldsets = (
        (None, {'fields':('EmailId','name','gender','Age','Aadhar_Number','ContactNumber','RecoveryMail','RecoveryNumber'
                          ,'Longitude','Latitude','City')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    #Below add_fieldsets are for adding new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':('EmailId','name','gender','Age','Aadhar_Number','ContactNumber','RecoveryMail','RecoveryNumber',
                      'Longitude','Latitude','City' ,'Address',
                      'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('EmailId',)
    ordering = ('EmailId',)

# @admin.register(models.PersonInNeed)
class VenueAdmin(admin.ModelAdmin):
    #'Action_taken_at',
    list_display = ('person','Longitude', 'Latitude','City','Address','Added_at','audio','Action_taken')
    list_filter = ('person', 'Latitude', 'Action_taken')
    ordering = ('Action_taken','Latitude')
    search_fields = ('person','Action_taken')

class AudioAdmin(admin.ModelAdmin):
    #'Action_taken_at',
    list_display = ('name','aud')
    # list_filter = ('person', 'Latitude', 'Action_taken')
    # ordering = ('Action_taken','Latitude')
    # search_fields = ('person','Action_taken')


admin.site.register(People, CustomUserAdmin)
admin.site.register(models.PersonInNeed,VenueAdmin)
admin.site.register(models.Audio,AudioAdmin)