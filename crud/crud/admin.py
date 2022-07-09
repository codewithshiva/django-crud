from django.contrib import admin
from crud.models import MoviesModel
from crud.models import GenreModel

class MoviesAdmin(admin.ModelAdmin):
    pass
class GenreAdmin(admin.ModelAdmin):
    pass


admin.site.register(MoviesModel,MoviesAdmin)
admin.site.register(GenreModel,GenreAdmin)