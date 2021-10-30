!alias bladesong embed <drac2>
ch=character()
cc="Bladesong"
ign=argparse(&ARGS&).get("i")
x=ch.cc_exists(cc) or ign
v=ign or ch.get_cc(cc) if x else False
n='\n'

ch.mod_cc(cc,-1) if v and not ign else ''

title = f""" -title "{name} {'invokes' if v else 'tries to invoke'} {cc}!"  """

desc = f""" -desc "{f'You gain a +{intelligenceMod} bonus to your AC, your walking speed increases by 10 feet, you have advantage on Dexterity (Acrobatics) checks, and you gain a +{intelligenceMod} bonus to any Constitution saving throws you make to maintain concentration on a spell' if v else 'You need a short or long rest before you can use this feature again'}"  """

if v:
    desc+=f""" -f "AC | {ch.ac+intelligenceMod}" """

field = f""" -f "{cc}{' (-1)' if v and not ign else ''}|{ch.cc_str(cc) if x else '**No Counter**'}" """

footer = f""" -footer "{ctx.prefix}{ctx.alias} [-i] {n}Created by RoyaleWithCheese with lots of help from Stab Lord, Reverend and Darth Frog" """

if (c:=combat()) and c.me and v:
    me=c.me
    me.add_effect(f"Bladesong","-ac +{intelligenceMod} -sadv 'dex'",10)

return f"{title} {desc} {field} -thumb {image} -color {color} {footer}"

</drac2>