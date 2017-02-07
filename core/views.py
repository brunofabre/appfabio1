from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'pages/home.html'


class AboutView(generic.TemplateView):
    template_name = 'pages/about.html'


class GamesView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/games.html'


class RankingView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/ranking.html'


class HistoryView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/history.html'


class TeamView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'pages/team.html'

home = HomeView.as_view()
about = AboutView.as_view()
games = GamesView.as_view()
ranking = RankingView.as_view()
history = HistoryView.as_view()
team = TeamView.as_view()
