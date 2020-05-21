from django.db import models


class Status(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        ordering = ['type']

    def __str__(self):
        return self.type


class Payment(models.Model):
    number = models.IntegerField()
    amount = models.IntegerField()
    aim = models.CharField(max_length=200)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_published']

    def __str__(self):
        return self.number
