from django.contrib import admin
from .models import Path_csv, Fields
# Register your models here.


@admin.register(Path_csv)
class Path_csvAdmin(admin.ModelAdmin):
    pass

@admin.register(Fields)
class FieldsAdmin(admin.ModelAdmin):
    pass