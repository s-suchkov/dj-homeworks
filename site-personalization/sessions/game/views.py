from django.shortcuts import render
from .models import Player, Game, PlayerGameInfo
import random

def show_home(request):

    if len(Game.objects.all().filter(status=False)) == 0:
        number = random.randint(0, 100)
        player = Player.objects.create(name='author')
        game = Game.objects.create(number=number, status=False)
        info = PlayerGameInfo.objects.create(player=player, game=game, counter=0, author=True)

        request.session['player_id'] = player.id
        request.session['game_id'] = game.id

    if ('player_id' and 'game_id') in request.session:
        if request.session['game_id'] == Game.objects.get(status=False).id:
            if PlayerGameInfo.objects.get(game__status=False).author==False:
                game = Game.objects.get(status=False)
                game.status = True
                game.save()
                if game.status:
                    del request.session['player_id']
                    del request.session['game_id']
                info = PlayerGameInfo.objects.filter(game__status=True).get(author=False)
                info.author = True
                info.save()
            else:
                info = PlayerGameInfo.objects.filter(game__status=False).get(author=True)
                info.player.name = 'author'
        else:
            del request.session['player_id']
            del request.session['game_id']
            info = PlayerGameInfo.objects.get(game__status=False)
        return render(
            request,
            'home.html',
            {'info': info,
            'counter': info.counter}
        )
    else:
            info = PlayerGameInfo.objects.get(game__status=False)
            info.player.name = 'Player'
            if PlayerGameInfo.objects.get(game__status=False).author == False:
                game = Game.objects.get(status=False)
                game.status = True
                game.save()
            # info.author = False
            info.counter += 1
            info.save()
            num = request.POST.get('number', default=None)
            if num == None:
                num = 0
            num = int(num)
            if num < info.game.number:
                hint = f'Загаданое число больше {num}'
            elif num > info.game.number:
                hint = f'Загаданое число меньше {num}'
            else:
                hint = 'Вы угадали число'
                info.author = False
                info.save()
                # game = Game.objects.get(status=False)
                # game.status = True
                # game.save()
            return render(
                request,
                'home.html',
                {'info': info,
                'hint': hint}
            )





