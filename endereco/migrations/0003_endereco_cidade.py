# Generated by Django 3.1.5 on 2021-01-14 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0002_remove_endereco_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(default=0.0011386138613861385, max_length=255),
            preserve_default=False,
        ),
    ]
