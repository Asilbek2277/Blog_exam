from django.contrib.auth.models import User, AbstractUser
from django.db import models



class Muallif(models.Model):
    name=models.CharField(max_length=50)
    yosh=models.PositiveSmallIntegerField()
    kasbi=models.CharField(max_length=40)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Maqola(models.Model):
    sarlavha=models.TextField()
    sana=models.DateField()
    mavzu=models.TextField()
    matn=models.TextField()
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha