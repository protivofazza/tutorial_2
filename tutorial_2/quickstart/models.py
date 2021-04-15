from django.db import models


class Tariffs(models.Model):
    info_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name


class States(models.Model):
    info_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.state


class Users(models.Model):
    info_id = models.AutoField(primary_key=True)
    agg_id = models.TextField(null=True, blank=True)
    family_name = models.TextField(null=True, blank=True)
    first_name = models.TextField(null=True, blank=True)
    account = models.TextField(null=True, blank=True)
    state = models.ForeignKey(States, null=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(Tariffs, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.family_name} {self.first_name}"
