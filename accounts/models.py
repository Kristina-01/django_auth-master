from django.db import models


class UserModel(models.Model):
    iduser = models.IntegerField (blank = True , null = True, default=0)
    name = models.CharField(max_length=100)
    lessonsmax = models.IntegerField(blank=True, null=True, default=1)
    pathimg = models.CharField(max_length=1000, default="{% static 'img/user.svg'%}")

    class Meta:
        managed = True
        db_table = 'accounts'