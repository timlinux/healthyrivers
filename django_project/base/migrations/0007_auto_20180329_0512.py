# Generated by Django 2.0.3 on 2018-03-29 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20180328_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationContext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context_document', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='locationsite',
            name='location_context',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.LocationContext'),
        ),
    ]