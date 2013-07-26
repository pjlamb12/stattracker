from django.shortcuts import render, get_object_or_404
from player.models import Player
from django import forms


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


def detail(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    context = {'player': player}
    return render(request, 'player/detail.html', context)