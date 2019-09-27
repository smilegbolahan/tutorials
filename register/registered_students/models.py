from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldRowPanel, FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

# Create your models here.

class FormField(AbstractFormField):
    page = ParentalKey(
        "FormPage", 
        on_delete = models.CASCADE,
        related_name = "form_fields", 
    ) 

class FormPage(AbstractEmailForm):
    template = "registered_students/registered_students.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address", classname="col6"),
                FieldPanel("to_address", classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="student_details"),
        

    ]