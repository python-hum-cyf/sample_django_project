from django.contrib import admin
from .models import Author

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ('name', 'year_of_birth', 'year_of_death', 'country_of_origin', 'years_of_life')
    list_display = ('name', 'year_of_birth', 'year_of_death')
    readonly_fields = ['years_of_life']

    def years_of_life(self, obj):
        if obj.year_of_birth is None or obj.year_of_death is None:
            return 'Unknown'
        return obj.year_of_death - obj.year_of_birth


