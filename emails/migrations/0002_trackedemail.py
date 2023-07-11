from __future__ import unicode_literals
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('message_id', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=9)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]