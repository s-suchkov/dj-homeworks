from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            form.cleaned_data

            print(form.cleaned_data)
            if len(form.cleaned_data) != 0:
                if form.cleaned_data['scope'].is_main:
                    count += 1
        if count != 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()

class RelationshipInline(admin.TabularInline):
    model = Scope.article.through
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
