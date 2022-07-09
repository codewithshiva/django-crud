from django.contrib import admin
from crud.models import MoviesModel

class MoviesAdmin(admin.ModelAdmin):
    pass


admin.site.register(MoviesModel,MoviesAdmin)