!alias dtcheck embed <drac2>
args,ch = &ARGS&, character()
if not len(args) >= 2:
  return "You must pass a Counter and Skill to use."
ch = character()
thresholds = [(0,10),(20,12),(40,14),(60,16),(80,18)]
results = []
rolls = []

for loop in range(argparse(args).last('rr',1,int)):

    cc = ([x for x in ch.consumables if args[0].lower() in x.name.lower()]+[None])[0]
    if not cc:
          err(f"Counter `{args[0]}` not found.")

    skill = ([x for x in ch.skills if args[1].lower() in x[0]]+[None])[0]
    if not skill:
          err(f"`{args[1]}` not found.")

    for val in thresholds:
          if cc.value >= val[0]:
                dc = val[1]
          else:
                break;

    Dice = vroll(skill[1].d20())

    rolls.append(Dice.total)

    if Dice.total >= dc:
          character().mod_cc(cc.name, 1)
          results.append(Dice.total)

T = f"{name} makes a {skill[0].replace('H',' H').title().replace('O',' O')} check!"
F = f"Total rolls: {len(rolls)}| {name} made **{len(results)}** successful checks!\n\n Results are: **{results}**. \n\n Total successes are **{cc.value}**" 
</drac2>
-title "{{T}}"
-f "{{F}}"
-color <color>
-thumb <image>