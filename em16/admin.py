from django.contrib import admin
from em16.models import Team, Game, Stadium, Round, Group


# Register your models here.
class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    list_display_links = ['group']
    list_editable = ['name']

    class Meta:
        model = Team


class SpieleModelAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'round', 'teamHomeAlias', 'teamGuestAlias', 'teamHome', 'teamHomeGoals',
                    'teamGuest', 'teamGuestGoals']
    list_display_links = ['date']
    list_editable = ['time', 'teamHomeAlias', 'teamGuestAlias', 'round', 'teamHome', 'teamHomeGoals', 'teamGuest',
                     'teamGuestGoals']

    class Meta:
        model = Game


class StadiumModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'capacity']
    list_display_links = ['name']
    list_editable = ['city', 'capacity']

    class Meta:
        model = Stadium


admin.site.register(Team, TeamModelAdmin)
admin.site.register(Game, SpieleModelAdmin)
admin.site.register(Stadium, StadiumModelAdmin)
admin.site.register(Round)
admin.site.register(Group)
# admin.site.register(Game, GameModelAdmin)
