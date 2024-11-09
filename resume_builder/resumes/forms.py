from django import forms
from .models import Profile, Education, Experience, Skill, Project, ExtraCurricular

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'summary', 'linkedin', 'github']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_date', 'end_date']

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'title', 'start_date', 'end_date', 'responsibilities']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'technologies', 'description']

class ExtraCurricularForm(forms.ModelForm):
    class Meta:
        model = ExtraCurricular
        fields = ['name', 'description']
