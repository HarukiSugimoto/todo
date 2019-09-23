from django.db import models

# Create your models here.
class Login(models.Model):
    mail_address = models.EmailField()
    password = models.CharField(max_length=10)

class Register(models.Model):
    user_name = models.CharField(max_length=10)
    mail_address = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

class Schedule(models.Model):
    Year_Choice = (
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    )
    Month_Choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        )
    Date_Choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    )
    user_name = models.CharField(max_length=10)
    year = models.CharField(max_length=2, choices=Year_Choice)
    month = models.CharField(max_length=2, choices=Month_Choice)
    day = models.CharField(max_length=2, choices=Date_Choice)
    date = models.DateTimeField()
    action = models.TextField()

    def __str__(self):
        return self.user_name