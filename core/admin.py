from django.contrib import admin
from core.models import *


# yıldız ile core içindeki her şeyi import ettik.

# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'job_description', 'job_title', 'job_location', 'start_date', 'end_date', 'updated_date',
                    'created_date']
    search_fields = ['company_name', 'job_title', 'job_location']
    list_editable = ['company_name', 'job_title', 'job_location', 'start_date', 'end_date', ]

    class Meta:
        model = Experience
        
        
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'percentage', 'updated_date', 'created_date']
    search_fields = ['name']
    list_editable = ['name', 'percentage']

    class Meta:
        model = Skill


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'classText', 'updated_date', 'created_date']
    search_fields = ['name', 'link', 'classText']
    list_editable = ['name', 'link', 'classText']

    class Meta:
        model = SocialMedia
        
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'proficiency', 'updated_date', 'created_date']
    search_fields = ['name', 'proficiency']
    list_editable = ['name', 'proficiency']

    class Meta:
        model = Language
        
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'school_name', 'department', 'start_date', 'end_date', 'updated_date', 'created_date']
    search_fields = ['school_name', 'department']
    list_editable = ['school_name', 'department', 'start_date', 'end_date']

    class Meta:
        model = Education
        
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_date', 'end_date', 'updated_date', 'created_date']
    search_fields = ['name', 'description']
    list_editable = ['name', 'description', 'start_date', 'end_date']

    class Meta:
        model = Activity