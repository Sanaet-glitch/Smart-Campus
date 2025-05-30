# Generated by Django 4.2.20 on 2025-04-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_enrollmentkey_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending Approval'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=16),
        ),
        migrations.AddField(
            model_name='enrollmentkey',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollmentkey',
            name='previous_key',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='enrollmentkey',
            name='regenerated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
