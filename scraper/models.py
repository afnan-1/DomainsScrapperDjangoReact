from django.db import models

# Create your models here.
class RandomDomainGenerator(models.Model):
    domain = models.CharField(max_length=50, blank=True,null=True)

    def __str__(self):
        return self.domain

class GodaddyAppraisal(models.Model):
    domain = models.CharField(max_length=50,unique=True)
    estimated_price = models.IntegerField()

    def __str__(self):
        return self.domain

class ScrapedDeletedDomain(models.Model):
    domain = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.domain