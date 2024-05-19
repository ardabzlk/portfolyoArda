from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import (models)


class AbstractModel(models.Model):
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="Updated Date"
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name="Created Date"
    )

    class Meta:
        abstract = True


class GeneralSetting(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text='This is the variable of the setting.'
    )
    description = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Description"
    )
    parameter = models.CharField(
        default='',
        max_length=512,
        blank=True,
        verbose_name="Parameter"
    )

    def __str__(self):
        return f'General Setting: {self.name}'
    
    class Meta:
        app_label = 'core'
        verbose_name = 'General Setting'
        verbose_name_plural = 'General Settings'
        ordering = ('name',)


class Experience(AbstractModel):
    company_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Company Name",
    )
    job_description = models.TextField(
        default='',
        blank=True,
        verbose_name="Job Description",
    )
    job_title = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Job Title",
    )
    job_location = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Job Location",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date",
    )

    def __str__(self):
        return f'Experience: {self.company_name}'

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ('-start_date',)



class Skill(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text='This is the variable of the setting.'
    )
    percentage = models.IntegerField(
        default=50,
        verbose_name="Percentage",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f'Skill: {self.name}'

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ('percentage',)

class SocialMedia(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text='This is the variable of the setting.'
    )
    link = models.URLField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Link"
    )
    classText = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Class Text"
    )

    def __str__(self):
        return f'Social Media: {self.name}'

    class Meta:
        verbose_name = 'Social Media'
        verbose_name_plural = 'Social Medias'
        ordering = ('name',)
        
        
class Language(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text='This is the variable of the setting.'
    )
    proficiency = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Proficiency"
    )

    def __str__(self):
        return f'Language: {self.name}'

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Activity(AbstractModel):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Name Test",
        help_text='This is the variable of the setting.'
    )
    description = models.TextField(
        default='',
        blank=True,
        verbose_name="Description",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date",
    )

    def __str__(self):
        return f'Activity: {self.name}'

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'
        ordering = ('-start_date',)
        
class Education(AbstractModel):
    school_name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="School Name",
    )
    department = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name="Department",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    end_date = models.DateField(
        default=None,
        null=True,
        blank=True,
        verbose_name="End Date",
    )

    def __str__(self):
        return f'Education: {self.school_name}'

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('-start_date',)