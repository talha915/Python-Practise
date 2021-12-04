from django.db import models

# Create your models here.
class MyTest(models.Model):
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    person_name = models.CharField(max_length=250, null=False, blank=False)

    # class Meta:
    #     db_table = 'training"."my_test'

    def __str__(self):
        return f'{self.person_name} '    