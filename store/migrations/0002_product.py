# Generated by Django 4.2.6 on 2024-01-15 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('product_image', models.ImageField(null=True, upload_to='images')),
                ('quantity', models.IntegerField()),
                ('original_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('description', models.TextField(max_length=300)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]