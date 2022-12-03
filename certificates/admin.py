from django.contrib import admin
from .models import Events, Templates, Fields
from django.utils.translation import ugettext_lazy as _


class FieldsInline(admin.TabularInline):
    model = Fields


@admin.register(Templates)
class TemplatesAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'title', 'file',
            ),
        }),
        (_('Header settings'), {
            'fields': (
                'headerfont', 'headersize', 'headerln', 'headermtop',
            ),
        }),
        (_('Text settings'), {
            'fields': (
                'textfont', 'textsize', 'textln', 'textmtop',
            ),
        }),
    )



@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    inlines = [FieldsInline,]
