from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('api', '0003_auto_20250707_1403'),  
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, default='Room'),
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]