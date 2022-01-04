from django.db import models

class country(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class states(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class district(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class town(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class zipcode(models.Model):
    country=models.ForeignKey(country, on_delete=models.CASCADE)
    state=models.ForeignKey(states, on_delete=models.CASCADE)
    district=models.ForeignKey(district, on_delete=models.CASCADE)
    town=models.ForeignKey(town, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
