import click as c
import random

N_DICE = 5
FILEPATH = 'eff_large_wordlist.txt'
words = {}


def import_words():
    with open(FILEPATH, 'r') as file:
        for line in file:
            dice, word = line.split()
            words[dice] = word


def roll_die():
    return random.randint(1, 6)


def roll_dice(n_times=N_DICE):
    dice = []
    for _ in range(n_times):
        dice.append(str(roll_die()))
    return "".join(dice)


@c.group()
def cli():
    import_words()


@cli.command()
@c.option('--num-of-words', '-n', 'num',
          default=6, show_default=True,
          help="Number of random words used.")
@c.option('--seperator', '-s', 'sep', default='')
@c.option('--case', '-c', 'case',
          type=c.Choice(['upper', 'lower', 'camel'],
                        case_sensitive=False), default='lower')
@c.option('--caps/--no-caps')
@c.option('--symbols/--no-symbols')
@c.option('--min-length')
@c.option('--max-length')
def diceware(num, sep, case, caps, symbols, min_length, max_length):
    passwords = []
    for _ in range(num):
        code = roll_dice()
        passwords.append(words[code])
    c.echo(f"Your new password is:\t{sep.join(passwords)}")

# TODO modify case
# TODO save (different APIs)
# TODO copy to clipboard
# TODO reroll
# TODO implement requirement checks
# TODO implement other password schemas
