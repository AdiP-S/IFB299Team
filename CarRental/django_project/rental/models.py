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

class Orders(models.Model):
    order_id = models.IntegerField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    order_createdate = models.IntegerField(db_column='Order_CreateDate')  # Field name made lowercase.
    order_pickupdate = models.IntegerField(db_column='Order_PickupDate')  # Field name made lowercase.
    order_pickupstore = models.IntegerField(db_column='Order_PickupStore')  # Field name made lowercase.
    pickup_store_name = models.CharField(db_column='Pickup_Store_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pickup_store_address = models.CharField(db_column='Pickup_Store_Address', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pickup_store_phone = models.CharField(db_column='Pickup_Store_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pickup_store_city = models.CharField(db_column='Pickup_Store_City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pickup_store_state_name = models.CharField(db_column='Pickup_Store_State_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    order_returndate = models.IntegerField(db_column='Order_ReturnDate')  # Field name made lowercase.
    order_returnstore = models.IntegerField(db_column='Order_ReturnStore')  # Field name made lowercase.
    return_store_name = models.CharField(db_column='Return_Store_Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    return_store_address = models.CharField(db_column='Return_Store_Address', max_length=25, blank=True, null=True)  # Field name made lowercase.
    return_store_phone = models.CharField(db_column='Return_Store_Phone', max_length=25, blank=True, null=True)  # Field name made lowercase.
    return_store_city = models.CharField(db_column='Return_Store_City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    return_store_state = models.CharField(db_column='Return_Store_State', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('order_id', 'order_createdate'),)

class Rentaldatabase(models.Model):
    order_id = models.IntegerField(db_column='Order_ID', primary_key=True)  # Field name made lowercase.
    order_createdate = models.IntegerField(db_column='Order_CreateDate')  # Field name made lowercase.
    order_pickupdate = models.IntegerField(db_column='Order_PickupDate')  # Field name made lowercase.
    order_pickupstore = models.IntegerField(db_column='Order_PickupStore')  # Field name made lowercase.
    pickup_store_name = models.CharField(db_column='Pickup_Store_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pickup_store_address = models.CharField(db_column='Pickup_Store_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pickup_store_phone = models.CharField(db_column='Pickup_Store_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pickup_store_city = models.CharField(db_column='Pickup_Store_City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pickup_store_state_name = models.CharField(db_column='Pickup_Store_State_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_returndate = models.IntegerField(db_column='Order_ReturnDate')  # Field name made lowercase.
    order_returnstore = models.IntegerField(db_column='Order_ReturnStore')  # Field name made lowercase.
    return_store_name = models.CharField(db_column='Return_Store_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    return_store_address = models.CharField(db_column='Return_Store_Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    return_store_phone = models.CharField(db_column='Return_Store_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    return_store_city = models.CharField(db_column='Return_Store_City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    return_store_state = models.CharField(db_column='Return_Store_State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_id = models.IntegerField(db_column='Customer_ID')  # Field name made lowercase.
    customer_name = models.CharField(db_column='Customer_Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_phone = models.CharField(db_column='Customer_Phone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_addresss = models.CharField(db_column='Customer_Addresss', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_brithday = models.DateTimeField(db_column='Customer_Brithday', blank=True, null=True)  # Field name made lowercase.
    customer_occupation = models.CharField(db_column='Customer_Occupation', max_length=12, blank=True, null=True)  # Field name made lowercase.
    customer_gender = models.CharField(db_column='Customer_Gender', max_length=5, blank=True, null=True)  # Field name made lowercase.
    car_id = models.IntegerField(db_column='Car_ID')  # Field name made lowercase.
    car_makename = models.CharField(db_column='Car_MakeName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_model = models.CharField(db_column='Car_Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_series = models.CharField(db_column='Car_Series', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_seriesyear = models.CharField(db_column='Car_SeriesYear', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_pricenew = models.CharField(db_column='Car_PriceNew', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_enginesize = models.CharField(db_column='Car_EngineSize', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_fuelsystem = models.CharField(db_column='Car_FuelSystem', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_tankcapacity = models.CharField(db_column='Car_TankCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_power = models.CharField(db_column='Car_Power', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_seatingcapacity = models.CharField(db_column='Car_SeatingCapacity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_standardtransmission = models.CharField(db_column='Car_StandardTransmission', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_bodytype = models.CharField(db_column='Car_BodyType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_drive = models.CharField(db_column='Car_Drive', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_wheelbase = models.CharField(db_column='Car_Wheelbase', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rentaldatabase'
        unique_together = (('order_id', 'customer_id'),)
