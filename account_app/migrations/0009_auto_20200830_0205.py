# Generated by Django 3.0.7 on 2020-08-29 19:05

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0008_auto_20200829_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurikulum',
            name='deskripsi',
            field=django_quill.fields.QuillField(),
        ),
    ]
