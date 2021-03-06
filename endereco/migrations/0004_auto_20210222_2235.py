# Generated by Django 3.1.5 on 2021-02-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endereco', '0003_endereco_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=models.CharField(max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(max_length=20, verbose_name='Cep'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(max_length=255, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='logradouro',
            field=models.CharField(max_length=255, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='numero',
            field=models.CharField(default='0', max_length=255, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='uf',
            field=models.CharField(max_length=255, verbose_name='Estado'),
        ),
    ]
