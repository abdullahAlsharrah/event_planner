from datetime import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator,MinValueValidator,MaxValueValidator

# Create your models here.

def validate_event(value):
    if value.lower() == "event":
        raise ValidationError("Sorry, cannot add the word event in the name")
    else:
        return value

# def validate_seats(value):
#     if value<5:
#         raise ValidationError("Sorry, number of seats cannot be less than 5")
#     else:
#         return value

emailvalidator = EmailValidator(message="invalid email")


class Event(models.Model):
    organizer = models.CharField(max_length=20)
    name = models.CharField(max_length=250, validators=[validate_event])
    email = models.CharField(max_length=250,blank=False,validators=[emailvalidator] )
    image = models.CharField(max_length=250,blank=False)
    num_of_seats = models.IntegerField(validators=[MinValueValidator(5)])
    booked_seats = models.IntegerField(default=0, )
    start_date = models.DateField(auto_created=False)
    end_date = models.DateField(auto_created=False)

    def check_booked(self):
        if self.num_of_seats < self.booked_seats:
            raise ValidationError("Booked Seats Cannot be Larger than Number of Seats")
        elif str(self.start_date) < str(datetime.today()):
            raise ValidationError("Start Date Cannot be before Today date")
        elif self.start_date > self.end_date:
            raise ValidationError("Start Date Cannot be after than End Date")

    def save(self, *args, **kwargs):
        self.check_booked()
        return super().save(*args, **kwargs)
        
