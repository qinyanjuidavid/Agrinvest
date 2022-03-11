# Generated by Django 4.0.2 on 2022-03-11 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmers', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=157, verbose_name='item')),
                ('quantity', models.FloatField(default=0.0, help_text='Number of Kgs available')),
                ('image', models.ImageField(upload_to='products/%y%m/%d')),
                ('price', models.FloatField(verbose_name='price')),
                ('approve', models.BooleanField(default=True, verbose_name='approve')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('on_stock', models.BooleanField(default=True, verbose_name='on stock')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farmers.productcategory')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.dealer')),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
