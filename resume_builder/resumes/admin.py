from django.contrib import admin

# Register your models here.
# from django.contrib import admin
from .models import Profile, Education, Experience, Skill, Project, ExtraCurricular

# Inline classes to display related entries under Profile in the admin panel
class EducationInline(admin.TabularInline):
    model = Education
    extra = 1  # Number of empty forms displayed initially

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class ExtraCurricularInline(admin.TabularInline):
    model = ExtraCurricular
    extra = 1

# Custom admin for Profile, with inlines for related models
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'linkedin', 'github')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('name',)

    # Inlines to display related models under Profile
    inlines = [EducationInline, ExperienceInline, SkillInline, ProjectInline, ExtraCurricularInline]

    # Customize the form layout for the Profile model
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'email', 'phone', 'linkedin', 'github')
        }),
        ('Summary', {
            'fields': ('summary',),
            'classes': ('collapse',),
        }),
    )

    class Media:
        css = {
            'all': ('resumes/admin/custom_admin.css',)
        }
        js = ('resumes/admin/custom_admin.js',)
        
# Register the Profile model with its custom admin
admin.site.register(Profile, ProfileAdmin)
