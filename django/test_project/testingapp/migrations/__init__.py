from django.db.models.deletion
from django.conf import settings
from django.db import migrations,models

class Migration(migrations.Migration):
    
    initial = True
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    
    operations = [
        migrations.CreateModel(
        name= 'UserProfile',
        fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'))
            ('bio', models.TextField(blank=True))
            ('profile_picture', models.ImageField(blank=True, upload_to='profile_pictures/'))
            ('user', models.OneToOneField(on_delete= django.db.models.deletion.CASCADE,to=settings.AUTH_USER_MODEL)),
        ],
        ),
    ]
    