# Generated by Django 4.2.3 on 2023-07-31 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_invoicedetail_invoice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoicedetail',
            options={'ordering': ['description']},
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.DateField(default='2023-07-31', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='invoicedetail',
            unique_together={('invoice', 'description')},
        ),
    ]
