# Generated by Django 5.0.6 on 2024-05-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_socialmedia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('name', models.CharField(blank=True, default='', help_text='This is the variable of the setting.', max_length=254, verbose_name='Name Test')),
                ('proficiency', models.CharField(blank=True, default='', max_length=254, verbose_name='Proficiency')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ('proficiency',),
            },
        ),
    ]
