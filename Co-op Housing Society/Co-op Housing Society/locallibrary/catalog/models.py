from django.db import models
import uuid
# Create your models here.

class Society_Registration(models.Model):
    Society_ID=models.AutoField(primary_key=True)
    Society_Name=models.CharField(max_length=100,help_text="Enter a Society name")
    Socety_Address=models.CharField(max_length=50, help_text="Enter Society Address")
    No_of_Flats=models.IntegerField(help_text="Enter the number of flats")
    Occupied_Flats=models.IntegerField(help_text="Enter the number of occupied flats")
    No_of_Parking=models.IntegerField(help_text="Enter the number of parking")
    No_of_Member=models.IntegerField(help_text="Enter the number of people living in the building")
    
    class Meta:
        ordering=["Society_Name"]

    
    def __str__(self):
        return self.Society_Name

'''
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
'''

class Member_Registration(models.Model):
    Member_ID=models.AutoField(primary_key=True)
    Flat_No=models.CharField(max_length=5,help_text="Enter a Flat No")
    Owner_Name=models.CharField(max_length=30, help_text="Enter Owner Name")
    Purchase_Date=models.DateField(max_length=10, help_text="Enter the date of purchase")
    Mobile_No=models.IntegerField(help_text="Enter your Mobile Number")
    Email_ID=models.EmailField(max_length=50, help_text="Enter your Email ID")
    No_of_rooms=models.IntegerField(default='2',help_text="Enter the number of rooms you have")
    Parking=models.IntegerField(default='1',help_text="Enter the number of parking you have")
    
    class Meta:
        ordering=["Flat_No"]



    
    def derivate_field_1(self):
        #Here goes all ur stuff to calculated your field
        base_amt=300
        wat_amt=100
    
        value = self.No_of_rooms*100 +base_amt + wat_amt
    
        return value 

    


    def __str__(self):
        return self.Flat_No
    

class Notice(models.Model):
    Notice_No=models.AutoField(primary_key=True)
    No_of_Pages=models.IntegerField(help_text="Enter a No of pages")
    Content=models.CharField(max_length=200, help_text="Enter Content")
    Date_of_Issue=models.DateField(max_length=10, help_text="Enter the date of issue")
    Date_of_Expiry=models.DateField(max_length=10, help_text="Enter the date of expiry")
    
    
    class Meta:
        ordering=["Notice_No"]

    
    def __str__(self):
        return self.Content
            
class Complaint(models.Model):
    Complaint_No=models.AutoField(primary_key=True)
    Flat_No=models.ForeignKey('Member_Registration', on_delete=models.SET_NULL, null=True)
    Content=models.CharField(max_length=200, help_text="Enter Content")
    Date_of_Issue=models.DateField(max_length=10, help_text="Enter the date of issue")
    
    
    
    class Meta:
        ordering=["Complaint_No"]

    
    def __str__(self):
        return self.Content

class Rent_Registration(models.Model):
    Rent_ID=models.AutoField(primary_key=True)
    Flat_No=models.CharField(max_length=5,help_text="Enter a Flat No")
    Tenant_Name=models.CharField(max_length=30, help_text="Enter the Name of the person")
    Date_of_Lease=models.DateField(max_length=10, help_text="Enter the date when the lease will end")
    Mobile_No=models.IntegerField(help_text="Enter your Mobile Number")
    Email_ID=models.EmailField(max_length=50, help_text="Enter your Email ID")
    
    
    class Meta:
        ordering=["Flat_No"]

    
    def __str__(self):
        return self.Tenant_Name
            
