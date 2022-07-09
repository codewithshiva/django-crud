from django.db import models
from django.core.validators import MinLengthValidator
import datetime
class MoviesModel(models.Model):
    id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=60,blank=False,validators=[MinLengthValidator(3)])
    ReleaseDate=models.DateField(default=datetime.date.today)
    Genre=models.ForeignKey('self', on_delete=models.CASCADE)
    Price=models.DecimalField(max_digits=5, decimal_places=2)
    Ratings=models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return self.Title or ''