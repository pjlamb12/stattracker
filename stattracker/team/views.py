from django.shortcuts import render, get_object_or_404
from team.models import Team
from player.models import Player
from django import forms


class AddTeamForm(forms.Form):
    team_name = forms.CharField(max_length=200)


class AddPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    number = forms.CharField(max_length=200)
#     team_name = forms.CharField(max_length=200)


def index(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            team_list = Team.objects.all().order_by('-team_name')
            delete_team = team_list.get(pk=request.POST['delete-team'])
            delete_team.delete()
            team_list = Team.objects.all().order_by('-team_name')
            new_form = AddTeamForm()
            dictionary = {'team_list': team_list, 'form': new_form}
            render(request, 'team/index.html', dictionary)
        else:
            form = AddTeamForm(request.POST)
            if form.is_valid():
                new_team = Team()
                new_team.team_name = form.cleaned_data['team_name']
                new_team.save()
                team_list = Team.objects.all().order_by('-team_name')
                new_form = AddTeamForm()
                dictionary = {'team_list': team_list, 'form': new_form}
                render(request, 'team/index.html', dictionary)
    form = AddTeamForm()
    team_list = Team.objects.all().order_by('-team_name')
    context = {'team_list': team_list, 'form': form}
    return render(request, 'team/index.html', context)


def detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = AddPlayerForm(request.POST)
        if form.is_valid():
            new_player = Player()
            new_player.first_name = form.cleaned_data['first_name']
            new_player.last_name = form.cleaned_data['last_name']
            new_player.number = form.cleaned_data['number']
            new_player.save()
            team.players.add(new_player)
            new_form = AddPlayerForm()
            context = {'team': team, 'form': new_form}
            render(request, 'team/index.html', context)
    else:
        form = AddPlayerForm()
    team_players = team.
    available_players = Player.objects.exclude()
    context = {'team': team, 'form': form, 'available_players': available_players}
    return render(request, 'team/detail.html', context)







