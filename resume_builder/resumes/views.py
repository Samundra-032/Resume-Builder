from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
from .models import Profile, Education, Experience, Skill, Project, ExtraCurricular
from .forms import ProfileForm, EducationForm, ExperienceForm, SkillForm, ProjectForm, ExtraCurricularForm
from django.forms import modelformset_factory


# def home(request):
#     return HttpResponse("This is home page proceed to other url")

def home(request):
    html = "<h1>This is home page proceed to other url</h1>"
    return HttpResponse(html)

# def home(request):
#     return render(request, 'resume/create_resume.html')

def create_resume(request):
    # Formsets for handling multiple entries in each section
    EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1)
    ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=1)
    SkillFormSet = modelformset_factory(Skill, form=SkillForm, extra=1)
    ProjectFormSet = modelformset_factory(Project, form=ProjectForm, extra=1)
    ExtraCurricularFormSet = modelformset_factory(ExtraCurricular, form=ExtraCurricularForm, extra=1)

    if request.method == "POST":
        # Process form submissions
        profile_form = ProfileForm(request.POST)
        education_formset = EducationFormSet(request.POST, queryset=Education.objects.none())
        experience_formset = ExperienceFormSet(request.POST, queryset=Experience.objects.none())
        skill_formset = SkillFormSet(request.POST, queryset=Skill.objects.none())
        project_formset = ProjectFormSet(request.POST, queryset=Project.objects.none())
        activity_formset = ExtraCurricularFormSet(request.POST, queryset=ExtraCurricular.objects.none())

        # Validate and save each form if valid
        if profile_form.is_valid() and education_formset.is_valid() and experience_formset.is_valid() and skill_formset.is_valid() and project_formset.is_valid() and activity_formset.is_valid():
            profile = profile_form.save()  # Save the main profile

            # Save each formset entry and associate it with the profile
            for form in education_formset:
                edu = form.save(commit=False)
                edu.profile = profile
                edu.save()

            for form in experience_formset:
                exp = form.save(commit=False)
                exp.profile = profile
                exp.save()

            for form in skill_formset:
                skill = form.save(commit=False)
                skill.profile = profile
                skill.save()

            for form in project_formset:
                proj = form.save(commit=False)
                proj.profile = profile
                proj.save()

            for form in activity_formset:
                activity = form.save(commit=False)
                activity.profile = profile
                activity.save()

            # Prepare context data for PDF generation
            context = {
                'profile': profile,
                'educations': profile.educations.all(),
                'experiences': profile.experiences.all(),
                'skills': profile.skills.all(),
                'projects': profile.projects.all(),
                'activities': profile.activities.all(),
            }

            # Render the PDF template
            pdf_template = 'resumes/resume_template.html'
            html = render_to_string(pdf_template, context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
            pisa_status = pisa.CreatePDF(html, dest=response)

            # Check for errors during PDF generation
            if pisa_status.err:
                return HttpResponse('There was an error generating the PDF', status=500)

            return response  # Directly serve the PDF
    else:
        # Render the empty form for GET request
        profile_form = ProfileForm()
        education_formset = EducationFormSet(queryset=Education.objects.none())
        experience_formset = ExperienceFormSet(queryset=Experience.objects.none())
        skill_formset = SkillFormSet(queryset=Skill.objects.none())
        project_formset = ProjectFormSet(queryset=Project.objects.none())
        activity_formset = ExtraCurricularFormSet(queryset=ExtraCurricular.objects.none())

    return render(request, 'resumes/create_resume.html', {
        'profile_form': profile_form,
        'education_formset': education_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'project_formset': project_formset,
        'activity_formset': activity_formset,
    })
