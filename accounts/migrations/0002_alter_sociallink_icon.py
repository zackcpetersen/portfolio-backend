# Generated by Django 3.2.6 on 2022-02-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociallink',
            name='icon',
            field=models.CharField(help_text='Use material design icons prepended with "mdi-", see full list at https://materialdesignicons.com/', max_length=255),
        ),
    ]