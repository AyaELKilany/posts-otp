# Generated by Django 4.1.4 on 2023-01-03 12:19

from django.db import migrations, models
import django_otp.util
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unverified_email', models.EmailField(max_length=80, unique=True)),
                ('secret_key', models.CharField(default=user.models.default_key, help_text='Hex-encoded secret key to generate totp tokens.', max_length=40, unique=True, validators=[django_otp.util.hex_validator])),
                ('last_verified_counter', models.BigIntegerField(default=-1, help_text='The counter value of the latest verified token.The next token must be at a higher counter value.It makes sure a token is used only once.')),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]