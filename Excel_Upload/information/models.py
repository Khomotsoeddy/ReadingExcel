from django.db import models

# Create your models here.
class UserInformation(models.Model):
    first_name = models.TextField(null=False)
    last_name = models.TextField(null=False)
    date_of_birth = models.DateField(null=False)

class UploadFile(models.Model):
    excel_uploaded = models.FileField(upload_to = 'files')
