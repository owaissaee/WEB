from django.contrib import admin
from .models import (
    ResumeTemplate,
    Resume,
    ResumeSection,
    WorkExperience,
    TechnicalSkill,
    Education,
    Technology,
    Project,
    Certification,
    Award,
    Language,
)

# Register your models here.
admin.site.register(ResumeTemplate)
admin.site.register(Resume)
admin.site.register(ResumeSection)
admin.site.register(WorkExperience)
admin.site.register(TechnicalSkill)
admin.site.register(Education)
admin.site.register(Technology)
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Award)
admin.site.register(Language)
