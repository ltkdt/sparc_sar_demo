# Generated manually to fix missing DemData table

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DemData',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('geotiff_file', models.FileField(blank=True, null=True, upload_to='geotiffs/')),
            ],
        ),
    ]




