from django.contrib import admin
from .models import learning ,learningcatagory,LearningSeries
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

class LearningAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date",{"fields":["learning_title","learning_published"]}),
        ("Series", {"fields": ["learning_series"]}),
        ("Url", {"fields": ["learning_slug"]}),
        ("Content",{"fields":["learning_content"]})
    ]

    formfield_overrides = {
        models.TextField:{'widget':TinyMCE()}
    }


admin.site.register(LearningSeries)
admin.site.register(learningcatagory)

admin.site.register(learning , LearningAdmin)