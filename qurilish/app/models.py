from django.db import models

# Create your models here.


class Territory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hudud'
        verbose_name_plural = 'Hududlar'


class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    formed = models.CharField(max_length=100)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tashkilot'
        verbose_name_plural = 'Tashkilotlar'


class Building(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    floor = models.IntegerField()
    parking = models.BooleanField()
    playground = models.BooleanField()
    elevator = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Bino'
        verbose_name_plural = 'Binolar'