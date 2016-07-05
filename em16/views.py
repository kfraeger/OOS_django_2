from django.views import generic
from django.core.urlresolvers import reverse_lazy

from em16.models import Team, Player, Stadium, Game, Round, Group
from em16.forms import GameForm


# Create your views here.

class IndexRedirectView(generic.RedirectView):
    """A view that redirects to /em16/."""

    url = reverse_lazy('em16:index')


class TeamListView(generic.ListView):
    """A view of all teams."""

    template_name = 'em16/team-list.html'
    model = Team
    context_object_name = "teams"


class TeamDetailView(generic.DetailView):
    """A view of one team and related players"""

    model = Team
    template_name = 'em16/team-detail.html'

    def get_context_data(self, **kwargs):
        context = super(TeamDetailView, self).get_context_data(**kwargs)
        # context['players'] = Player.objects.filter(team_id=self.kwargs['pk']).order_by('team', 'surname')
        context['players'] = Player.objects.filter(team_id=self.kwargs['pk']).order_by('surname')
        return context


class TeamCreateView(generic.CreateView):
    """A view with a empty form to create a new team
       by success redirect to all teams
    """

    template_name = 'em16/forms/team_form.html'
    model = Team
    fields = ['name', 'short', 'group', 'trainer', 'flag']
    success_url = reverse_lazy('em16:team-list')


class TeamUpdateView(generic.UpdateView):
    """A view with a filled form to update a existing team
        by success redirect to settings of teams
    """

    model = Team
    template_name = 'em16/forms/team_update_form.html'
    fields = ['name', 'short', 'group', 'trainer', 'flag']
    success_url = reverse_lazy('em16:team-edit')


class TeamDeleteView(generic.DeleteView):
    """A view to delete existing team
        by success redirect to settings of teams
    """

    template_name = "em16/confirm/team_confirm_delete.html"
    model = Team
    success_url = reverse_lazy('em16:team-edit')


class PlayerCreateView(generic.CreateView):
    """A view with a empty form to create a new player to a certain team
        by success redirect to settings of teams
     """

    template_name = 'em16/forms/player_form.html'
    model = Player
    fields = ['team', 'name', 'surname', 'position', 'number', 'img']
    success_url = reverse_lazy('em16:team-edit')

    def get_initial(self):
        team = Team.objects.get(id=self.kwargs['pk'])
        return {
            'team': team,
        }


class PlayerUpdateView(generic.UpdateView):
    """A view with a filled form to update a existing player
        by success redirect to settings of teams
    """

    model = Player
    template_name = 'em16/forms/player_update_form.html'
    fields = ['team', 'name', 'surname', 'position', 'number', 'img']
    success_url = reverse_lazy('em16:team-edit')


class PlayerDeleteView(generic.DeleteView):
    """A view to delete existing player
        by success redirect to settings of teams
    """

    template_name = "em16/confirm/player_confirm_delete.html"
    model = Player
    success_url = reverse_lazy('em16:team-edit')


class GameListView(generic.ListView):
    template_name = 'em16/game_list.html'
    model = Game
    context_object_name = 'games'

    def get_context_data(self, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.all().order_by('group_id','-win', '-goal', 'goal_conceded')
        context['rounds'] = Round.objects.all()
        return context


class RoundDetailView(generic.DetailView):
    template_name = 'em16/round-detail.html'
    model = Round
    context_object_name = 'round'

    def get_context_data(self, **kwargs):
        context = super(RoundDetailView, self).get_context_data(**kwargs)
        context['rounds'] = Round.objects.all()
        context['games'] = Game.objects.filter(round_id=self.kwargs['pk']).order_by('date', 'time')
        return context


class GameCreateView(generic.CreateView):
    """A view with a empty form to create a new team
       by success redirect to all teams
    """

    template_name = 'em16/forms/game_form.html'
    form_class = GameForm
    success_url = reverse_lazy('em16:setting-list')


class GameUpdateView(generic.UpdateView):
    """A view with a empty form to create a new team
       by success redirect to all teams
    """
    model = Game
    template_name = 'em16/forms/game_update_form.html'
    fields = ['date', 'time', 'round', 'group', 'teamHome', 'teamGuest', 'teamHomeGoals', 'teamGuestGoals', 'others']
    success_url = reverse_lazy('em16:game-edit')


class GameDeleteView(generic.DeleteView):
    """A view to delete existing player
        by success redirect to settings of teams
    """

    template_name = "em16/confirm/game_confirm_delete.html"
    model = Game
    success_url = reverse_lazy('em16:game-edit')


class SettingsView(generic.TemplateView):
    """A view for all settings
     """

    template_name = 'em16/settings.html'


class SettingsTeamEditView(generic.ListView):
    """A view for all settings to all teams
     """

    template_name = 'em16/settings-team-edit.html'
    model = Team
    context_object_name = "teams"

    def get_context_data(self, **kwargs):
        context = super(SettingsTeamEditView, self).get_context_data(**kwargs)
        # context['players'] = Player.objects.all().order_by('team', 'surname')
        context['players'] = Player.objects.select_related('team').order_by('team', 'surname')
        return context


class SettingsGameEditView(generic.ListView):
    """A view for all settings to game schedule
     """

    template_name = 'em16/settings-game-edit.html'
    model = Game
    context_object_name = "games"


class SettingsGroupEditView(generic.ListView):
    """A view for all settings for groups
     """

    template_name = 'em16/settings-group-edit.html'
    model = Group
    context_object_name = "groups"

    def get_context_data(self, **kwargs):
        context = super(SettingsGroupEditView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.select_related('group').order_by('group', '-win', '-goal', 'goal_conceded')
        return context


class GroupListView(generic.ListView):
    """A view for all settings for groups
     """
    template_name = 'em16/group_list.html'
    model = Group
    context_object_name = "groups"

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        context['teams'] = Team.objects.select_related('group').order_by('group', '-win', '-goal', 'goal_conceded')
        context['games'] = Game.objects.all().order_by('group', 'date')
        return context


class GroupUpdateView(generic.UpdateView):
    """A view with a empty form to create a new team
       by success redirect to all teams
    """
    model = Team
    template_name = 'em16/forms/group_update_form.html'
    fields = ['games_played', 'win', 'draw', 'lost', 'goal', 'goal_conceded']
    success_url = reverse_lazy('em16:group-edit')


class StadiumList(generic.ListView):
    """A view of all stadiums."""

    template_name = 'em16/stadium-list.html'
    model = Stadium
    context_object_name = "stadiums"
