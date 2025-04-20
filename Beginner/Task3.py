justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

#Calculate the number of members in the Justice League. len() function is used.
print("Total Members :",len(justice_league))

#Batman recruited Batgirl and Nightwing as new members.Add them to your list. append() function is used.
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("The Justice League after recuriting Batgirl and Nightwing :",justice_league)

#Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove("Wonder Woman")
justice_league.insert(0,"Wonder Woman")
print("The list after making Wonder Woman as leader :",justice_league)

#Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman"and move them in between Aquaman and Flash.
justice_league.remove("Superman")
Flash_index=justice_league.index("Flash")
justice_league.insert(Flash_index+1,"Superman")
print("The list after separating Aquaman and Flash :",justice_league)

#The Justice League faced a crisis, and Superman decided to assemble a new team. Replace the existing list with the following new members: "Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow".
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("The new Justice League :",justice_league)

#Sort the Justice League alphabetically. The hero at the 0th index will become the new leader.
justice_league.sort()
print("The sorted list :",justice_league)

#BONUS: (Can you predict who the new leader will be?)
print("The leader of the new Justice League is ",justice_league[0])