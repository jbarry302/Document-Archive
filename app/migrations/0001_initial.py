# Generated by Django 5.0.2 on 2024-03-04 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('file_document', models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='File Document')),
                ('document_url', models.URLField(blank=True, null=True, verbose_name='Document URL')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='documents/', verbose_name='Picture')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
