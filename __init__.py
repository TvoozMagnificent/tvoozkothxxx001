from random import random, choice
from rich.live import Live
from rich.table import Table
from time import sleep
from random import shuffle
from funcopy import copy_func
BOTS = RICH = LEADERBOARD = MAIN = True
if RICH:

    from rich.console import Console
    from rich.table import Table
    console = Console()
    def print(*args, **kwargs): console.print(*args, **kwargs)
if LEADERBOARD:

    def copy(list_):
        if type(list_) is list:
            return [copy(i) for i in list_]
        else: return list_

    def leaderboard(info, title, round_):
        bots = [i[0] for i in info]
        b = sorted(bots, key=lambda x: (-info[bots.index(x)][1], -info[bots.index(x)][2]))
        x = max([*map(lambda bot:len(bot.__name__), b)])  +  3
        table = Table(show_header=True, header_style="bold #00ffff", title=title) # cyan
        table.add_column("Place", justify="right", style="bold #0000ff", width=5) # blue
        table.add_column("Bot",   justify="right", style="bold #ffff00", width=x) # yellow
        table.add_column("Score", justify="right", style="#00ff00",      width=8) # green
        table.add_column("Freq.", justify="right", style="#ff0000",      width=8) # red

        for index in range(len(b)):
            bot = b[index]
            table.add_row(str(index+1),
                          str(bot.__name__),
                          str(info[bots.index(bot)][1]),
                          str(round(info[bots.index(bot)][2],1)))
        return table
if MAIN:

    def main(BoTs=[], rounds=10000):

        def testbot(info, me, round):
            return [me, 0, 1]

        def randombot(info, me, round):
            return [choice([i[0] for i in info]), choice([0, 1]), choice([0, 1])]

        def paralyzer(info, me, round):
            turning_bots = [*filter(lambda x: x[2] > 0 and x[0] != me, info)]
            if turning_bots and random() < 0.8:
                return [turning_bots[0][0], 1, 0]
            else:
                return [me, 0, 1]

        def savers(info, me, round):
            _, score, freq = [i for i in info if i[0] == me][0]
            if freq < 2:
                return [me, 1, 1]
            else:
                return [me, 0, 1]

        def killer(info, me, round):
            turning_bots = sorted([*filter(lambda x: x[0] != me, info)], key=lambda x: -x[1])
            if turning_bots: return [turning_bots[0][0], 0, 0]
            return [me, 0, 1]

        BoTs += [testbot, randombot, paralyzer, savers, killer]

        # function such that given "function_name" it returns the function
        def get_function(function_name):
            # get the function using eval
            return eval(function_name)

        def clone_function(function):
            return copy_func(function)

        def clone_list(list_):
            return [clone_list(i) if type(i)==list else i for i in list_]

        def shuffled(list_):
            l = clone_list(list_)
            shuffle(l)
            return l

        bots = []
        for _ in range(10):
            bots+=[*map(clone_function, BoTs)]

        info = [[bot, 0, 1.0] for bot in bots]
        round = 0

        with Live(leaderboard(info, f"\n"
                                    f"[purple]Round [biu]{round}[/] completed. ", round),
                  refresh_per_second=100) as live:
            for round in range(1,rounds+1):
                for bot in shuffled(bots):
                    if random()<info[bots.index(bot)][2]:
                        # call the bot
                        response = bot(shuffled(copy(info)), bot, round)
                        # update the info
                        target, score, increase, *_ = response # *_ for compatibility
                        factor = 1 if increase else -1
                        factor *= 0.1 if score else 1
                        info[bots.index(target)][score+1] += factor
                live.update(leaderboard(info, f"\n"
                              f"[purple]Round [biu]{round}[/] completed. ", round))
            while True: pass
