from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customers_Rental(models.Model):
    customer_id = models.IntegerField(db_column='Customer_ID', default = 0)  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=12, blank=True, null=True)  # Field name made lowercase.
    customer_phone = models.CharField(db_column='Customer_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    customer_address = models.CharField(db_column='Customer_Address', max_length=45, default = '')  # Field name made lowercase.
    customer_birthday = models.DateTimeField(db_column='Customer_Birthday', blank=True, null=True)  # Field name made lowercase.
    customer_occupation = models.CharField(db_column='Customer_Occupation', max_length=12, blank=True, null=True)  # Field name made lowercase.
    customer_gender = models.CharField(db_column='Customer_Gender', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        unique_together=(('customer_id', 'customer_address'),)

    def __str__(self):
        return self.customer_name
