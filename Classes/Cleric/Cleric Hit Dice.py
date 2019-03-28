**Cleric HD**  
*By Sajison*  
  
This is for the Cleric Hit Dice  
  
`!cc create "Hit Dice" -reset long -max {{level}} -min 0 -type bubble`  
  
```py  
!alias hd embed {{set('roll', roll('1d8'))}} 
-title "<name> {{"attempts to use" if get_cc("Hit Dice")==0 else "uses"}} a Hit Die" -desc "They pause  {{"Nothing seems to happen, however. Perhaps they need to take long rest before trying again?" if get_cc("Hit Dice")==0 else "After a moment you feel better."}}" -f "{{"" if get_cc("Hit Dice")==0 else ""}}Hit Die heals for: {{"|" if get_cc("Hit Dice")==0 else "|"}} 1d8 ({{""+str(roll)+"" if roll==8 or roll==1 else roll}}) + {{constitutionMod}} = {{roll+constitutionMod}}{{set('healed', roll + currentHp + constitutionMod)}}.{{"" if get_cc("Hit Dice")==0 else ""}}" -f "Current HP: | {{currentHp if get_cc("Hit Dice")==0 else min(hp, healed)}}/{{hp}}{{"" if get_cc("Hit Dice")==0 else set_hp(min(hp, healed))}}" -thumb <image> {{"" if get_cc("Hit Dice")==0 else mod_cc("Hit Dice", -1)}}```





