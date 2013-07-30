from django.shortcuts import render, get_object_or_404
from player.models import Player
from statsheet.models import Statsheet
from django import forms
from django.utils import timezone


class AddPlayerForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    number = forms.CharField(max_length=200)
#     team_name = forms.CharField(max_length=200)



def index(request):
    if request.method == 'POST':
        if 'delete' in request.POST:
            player_list = Player.objects.order_by('-last_name')
            delete_player = player_list.get(pk=request.POST['delete-player'])
            delete_player.delete()
            player_list = Player.objects.order_by('-last_name')
            new_form = AddPlayerForm()
            context = {'player_list': player_list, 'form': new_form}
            render(request, 'player/index.html', context)
        else:
            form = AddPlayerForm(request.POST)
            if form.is_valid():
                new_player = Player()
                new_player.first_name = form.cleaned_data['first_name']
                new_player.last_name = form.cleaned_data['last_name']
                new_player.number = form.cleaned_data['number']
                new_player.save()
                new_form = AddPlayerForm()
                player_list = Player.objects.order_by('-last_name')
                context = {'player_list': player_list, 'form': new_form}
                render(request, 'player/index.html', context)
    form = AddPlayerForm()
    player_list = Player.objects.order_by('-last_name')
    context = {'player_list': player_list, 'form': form}
    return render(request, 'player/index.html', context)


class AddStatsheetForm(forms.Form):
    offensive_rebounds = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    defensive_rebounds = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    assists = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    points = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    steals = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    blocks = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))
    fouls = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input-xlarge'}))


def detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        if 'add' in request.POST:
            form = AddStatsheetForm(request.POST)
            if form.is_valid():
                new_statsheet = Statsheet()
                new_statsheet.player = player
                new_statsheet.game_day = timezone.now()
                new_statsheet.offensive_rebounds = form.cleaned_data['offensive_rebounds']
                new_statsheet.defensive_rebounds = form.cleaned_data['defensive_rebounds']
                new_statsheet.assists = form.cleaned_data['assists']
                new_statsheet.points = form.cleaned_data['points']
                new_statsheet.steals = form.cleaned_data['steals']
                new_statsheet.blocks = form.cleaned_data['blocks']
                new_statsheet.fouls = form.cleaned_data['fouls']
                new_statsheet.save()
                new_form = AddStatsheetForm()
                statsheets = Statsheet.objects.filter(player=player.id)
                context = {'player': player, 'form': new_form, 'statsheets':statsheets}
                return render(request, 'player/detail.html', context)
        else:
            statsheet_list = Statsheet.objects.all()
            delete_sheet = statsheet_list.get(pk=request.POST['delete-stats'])
            delete_sheet.delete()
            new_form = AddStatsheetForm()
            statsheets = Statsheet.objects.filter(player=player.id)
            context = {'player': player, 'form': new_form, 'statsheets':statsheets}
            return render(request, 'player/detail.html', context)
    form = AddStatsheetForm()
    statsheets = Statsheet.objects.filter(player=player.id)
    context = {'player': player, 'form':form, 'statsheets':statsheets}
    return render(request, 'player/detail.html', context)