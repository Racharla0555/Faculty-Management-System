# Generated by Django 4.1.3 on 2022-11-21 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_rename_achievements_faculty_faculty_achievements_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Achievements',
            new_name='Achievements',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Age',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Experience',
            new_name='Experience',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Mobile_Number',
            new_name='Mobile_Number',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Qualification',
            new_name='Qualification',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='Faculty_Subject',
            new_name='Subject',
        ),
    ]
