from django.db import models
from django.utils import timezone

# Three steps to updating the database:
# 1. Change your models (in models.py).
# 2. Run python manage.py makemigrations to create migrations for those changes
# 3. Run python manage.py migrate to apply those changes to the database.

# Create your models here.
class HostUser(models.Model):
    username = models.CharField(max_length=200)
    downloads = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class HostBoard(models.Model):
    owned_by = models.CharField(max_length=200)
    board_name = models.CharField(max_length=200)
    downloads = models.IntegerField(default=0)
    #download_date = models.DateTimeField('last downloaded')
    #def was_downloaded_recently(self):
    #    return self.download_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.board_name
