# Определим функцию, эмулирующую рыбалку
import random
from collections import defaultdict

FISH = (None, 'плотва', 'окунь', 'лещ')


# caught_fish = defaultdict(int)

def fishing(name, worms):
    catch = defaultdict(int)
    for worm in range(worms):
        # print(f'{name}: Червяк № {worm} - Забросил, ждем...', flush=True)
        _ = 3 ** (random.randint(50, 70) * 10000)
        fish = random.choice(FISH)
        if fish is None:
            # print(f'{name}: Тьфу, сожрали червяка...', flush=True)
            pass
        else:
            # print(f'{name}: Ага, у меня {fish}', flush=True)
            catch[fish] += 1
    # print(f'Итого рыбак {name} поймал:')
    for fish, count in catch.items():
        pass
        # print(f'    {fish} - {count}')
    return catch


caught_fish = dict(fishing(name='Вася', worms=10))
# print(caught_fish)
