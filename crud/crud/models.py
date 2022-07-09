from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class GenreModel(models.Model):
    Genre=models.CharField(max_length=60,primary_key=True)
    
    def __str__(self):
        return self.Genre or ''
class MoviesModel(models.Model):
    def validate_Ratings(value):
        if value >10:
            raise ValidationError(
            _('Ratings cannot be more than 10'),
            params={'value': value},
        )
    id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=60,blank=False,validators=[MinLengthValidator(3)])
    ReleaseDate=models.DateField(default=datetime.date.today)
    genre=models.ForeignKey('GenreModel',blank=False, on_delete=models.CASCADE)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Ratings=models.DecimalField(max_digits=3, decimal_places=1,validators=[validate_Ratings])
    
    def __str__(self):
        return self.Title
    
