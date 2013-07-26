from django.contrib import admin
from player.models import Player
from statsheet.models import Statsheet


class StatsInline(admin.StackedInline):
    model = Statsheet
    extra = 1


class PlayerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Player Information', {'fields': ['first_name', 'last_name', 'number']}),
    ]
    inlines = [StatsInline]
    search_fields = ['last_name']


admin.site.register(Player, PlayerAdmin)