from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from games.models import Game


class HomeView(generic.TemplateView):
    template_name = 'pages/home.html'


class AboutView(generic.TemplateView):
    template_name = 'pages/about.html'


class GamesView(LoginRequiredMixin, generic.ListView):
    model = Game
    context_object_name = 'games'
    template_name = 'pages/games.html'


class RankingView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/ranking.html'


class HistoryView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/history.html'


class TeamView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/team.html'


class PanelHomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'panel/home.html'


home = HomeView.as_view()
about = AboutView.as_view()
games = GamesView.as_view()
ranking = RankingView.as_view()
history = HistoryView.as_view()
team = TeamView.as_view()
panelhome = PanelHomeView.as_view()
