# Generated by Django 2.0.8 on 2018-08-29 16:24

from django.db import migrations, models
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorateStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='uploads/people/')),
                ('eng_name', models.CharField(max_length=100, verbose_name='English name')),
                ('zh_name', models.CharField(max_length=100, verbose_name='Chinese name')),
                ('email', models.EmailField(max_length=254)),
                ('research_interests', models.TextField()),
                ('year_of_study', models.CharField(choices=[('CURRENT', 'Current'), ('GRAD', 'Graduated')], default='CURRENT', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='uploads/faculty')),
                ('zh_name', models.CharField(blank=True, max_length=100, verbose_name='Chinese name')),
                ('eng_name', models.CharField(blank=True, max_length=100, verbose_name='English name')),
                ('title', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=1000)),
                ('research_interests', models.TextField()),
                ('cv_upload', models.FileField(blank=True, upload_to='uploads/faculty/cv')),
                ('status', models.CharField(choices=[('CURRENT', 'Current'), ('RETIRED', 'Retired')], default='CURRENT', max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Faculty',
            },
        ),
        migrations.CreateModel(
            name='MasterStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='uploads/people/')),
                ('eng_name', models.CharField(max_length=100, verbose_name='English name')),
                ('zh_name', models.CharField(max_length=100, verbose_name='Chinese name')),
                ('email', models.EmailField(max_length=254)),
                ('research_interests', models.TextField()),
                ('year_of_study', models.CharField(choices=[('FIRST', 'First'), ('SECOND', 'Second'), ('THIRD', 'Third'), ('FOURTH', 'Fourth'), ('GRAD', 'Graduated')], default='FIRST', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('office_hours', models.CharField(max_length=100)),
            ],
        ),
    ]
