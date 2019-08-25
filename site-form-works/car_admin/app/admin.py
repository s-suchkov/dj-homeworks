from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm
from ckeditor.widgets import CKEditorWidget




class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')
    # fields = ('brand', 'model', 'review_count')
    list_filter = ('brand', 'model')
    search_fields = ['brand', 'model']
    ordering = ['-id']



class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    list_filter = ('car', 'title', 'car__brand', 'car__model')
    search_fields = ['car__brand', 'car__model', 'title']
    ordering = ['-id']

admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
