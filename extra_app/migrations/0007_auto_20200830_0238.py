# Generated by Django 3.0.7 on 2020-08-29 19:38

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('extra_app', '0006_auto_20200828_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporanmurid',
            name='konten',
            field=django_quill.fields.QuillField(),
        ),
        migrations.AlterField(
            model_name='pengumuman',
            name='konten',
            field=django_quill.fields.QuillField(),
        ),
    ]
