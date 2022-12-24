from django.db import models


class Position(models.Model):
    doljnost = models.CharField(max_length=30)
    otdel = models.CharField(max_length=30)

    def __str__(self):
        return self.doljnost


class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.IntegerField()
    zarplata = models.IntegerField()

    def __str__(self):
        return f'{self.fullname}-{self.position}'
