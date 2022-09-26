# Generated by Django 3.1.2 on 2021-01-07 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210107_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='workschedule',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(blank=True, max_length=50000, null=True)),
                ('added', models.DateTimeField(auto_now=True)),
                ('reciever', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recieved_mails', to='core.websiteuser')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.websiteuser')),
            ],
            options={
                'verbose_name': 'Mail',
                'verbose_name_plural': 'Mails',
            },
        ),
    ]