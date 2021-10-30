embed <drac2>
a, n, ch = &ARGS&, '\n', character()
info = load_json(get_gvar("c0797393-af58-45df-ad95-11e56e92a5b0"))
feat = a[0] if a else ""
cc = "Leadership Dice"
x = ch.cc_exists(cc) and feat
v = ch.get_cc(cc) if x else False
fullFeat = ""


for loop in range(len(info)):
    if (info[loop].name == feat and v):
        fullFeat = info[loop]
        ch.mod_cc(cc,-1) if v else ''
        break
    else:
        continue

title = f""" -title "{name} {'invokes' if fullFeat else 'tries to invoke'} {fullFeat.name if fullFeat else feat if feat else 'a feat without passing any parameters' }!" """

desc = f""" -desc "{fullFeat.desc if fullFeat else 'You need to take a long or short rest before using this ability' if not v else 'The name you have passed is incorrect. This alias is case-sensitive'}" """

field = f""" -f "{cc}{' (-1)' if v and fullFeat else ''}|{ch.cc_str(cc) if x else '**No Counter**'}" """

footer = f""" -footer "{ctx.prefix}{ctx.alias} <name> {n}Created by RoyaleWithCheese#3039" """

return f"{title} {desc} -thumb {image} -color {color} {footer} {field}"
</drac2>