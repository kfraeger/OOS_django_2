"""djangoSS16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    # index
    url(r'^$', views.GameListView.as_view(), name="index"),

    # /teams/
    url(r'^teams/$', views.TeamListView.as_view(), name="team-list"),
    url(r'^teams/(?P<pk>\d+)/$', views.TeamDetailView.as_view(), name="team-detail"),

    # /rounds/
    url(r'^rounds/(?P<pk>\d+)/$', views.RoundDetailView.as_view(), name="round-detail"),

    # /stadiums/
    url(r'^stadiums/', views.StadiumList.as_view(), name="stadium-list"),

    # /groups/
    url(r'^settings/groups/$', views.GroupListView.as_view(), name="group-list"),


    # /settings/
    url(r'^settings/$', views.SettingsView.as_view(), name="setting-list"),

    # /settings/team/
    url(r'^settings/team/add/$', views.TeamCreateView.as_view(), name="team-create"),
    url(r'^settings/team/$', views.SettingsTeamEditView.as_view(), name="team-edit"),
    url(r'^settings/team/(?P<pk>\d+)/delete/$', views.TeamDeleteView.as_view(), name="team-delete"),
    url(r'^settings/team/(?P<pk>\d+)/update/$', views.TeamUpdateView.as_view(), name="team-update"),

    # /settings/team/player
    url(r'^settings/team/(?P<pk>\d+)/player/add/$', views.PlayerCreateView.as_view(), name="player-create"),
    url(r'^settings/team/player/(?P<pk>\d+)/delete/$', views.PlayerDeleteView.as_view(), name="player-delete"),
    url(r'^settings/team/player/(?P<pk>\d+)/update/$', views.PlayerUpdateView.as_view(), name="player-update"),

    # /settings/game
    url(r'^settings/game/add/$', views.GameCreateView.as_view(), name="game-create"),
    url(r'^settings/game/$', views.SettingsGameEditView.as_view(), name="game-edit"),
    url(r'^settings/game/(?P<pk>\d+)/delete/$', views.GameDeleteView.as_view(), name="game-delete"),
    url(r'^settings/game/(?P<pk>\d+)/update/$', views.GameUpdateView.as_view(), name="game-update"),

    # /settings/group/
    url(r'^settings/group/$', views.SettingsGroupEditView.as_view(), name="group-edit"),
    url(r'^settings/group/team/(?P<pk>\d+)/update/$', views.GroupUpdateView.as_view(), name="group-update"),


]