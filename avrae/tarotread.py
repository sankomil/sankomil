!alias tarotread embed
<drac2>
a, n = &ARGS&, '\n'
aps = argparse(a).last("aps")
g = load_json(get_gvar("e8d276b0-f173-4aa1-86e9-b5d5df2184c3")) if not aps else load_json(get_gvar("6c03a532-3293-45cd-a477-b5c2961e591c"))
d = "tarotDeck" if not aps else "apsTarotDeck"
setup = "set".lower() in a
deck = load_json(get(d,"[]"))
draw = "draw" in a and len(deck) > 0
size = 22 if setup and not aps else 14 if setup and aps else len(deck) if deck else 0
pos = argparse(a).last("position")
pos = int(pos) if draw and pos and int(pos) > 0 and int(pos) < size else ""

if setup:
    count = 0
    deck = []
    for c in g:
        deck.append(c)
        count = count + 1
        if count == size:
            break
      
shuffled=[]

while deck:
    shuffled.append(deck.pop(randint(len(deck))))  
    
deck = shuffled


pos = argparse(a).last("position")
pos = int(pos) if draw and pos and int(pos) > 0 and int(pos) < len(deck) else ""

cardName = deck[randint(len(deck)-1)] if draw and not pos else deck[pos] if pos else ""

card = g[cardName] if cardName else ""

if cardName:
    deck.remove(cardName)
    numCards = len(deck) - 1

if deck:
    set_cvar(d,dump_json(deck))
    

    
title = f""" -title "{name} {f"draws {card.name} from {pos} position in the deck" if pos else f"draws {card.name} from the deck" if draw else "sets up their Tarot deck" if setup else "needs help with their Tarot deck"}" """

desc = f""" -desc "{card.desc if draw else f"Start drawing with `{ctx.prefix}{ctx.alias} draw`" if setup else f"1. Set up with `{ctx.prefix}{ctx.alias} set`{n}2. Draw with `{ctx.prefix}{ctx.alias} draw`"}" """

cardImage = f""" -image "{f'http://i.imgur.com/{card.image}.png' if card else ""}" """

footer = f""" -footer "Tarot Draw | {ctx.prefix}{ctx.alias} set - Sets up the deck | {ctx.prefix}{ctx.alias} draw [-position #] - Draws a card {n}Created by RoyaleWithCheese#3039 and Panphoria#4915" """

return f"{title} {desc} {cardImage} -thumb {image} -color {color} {footer}"
return f"""{title}"""
</drac2>