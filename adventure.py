#Alan

print("Welcome to the Forest Adventure!")
print("You wake up in a mysterious forest. There are two paths ahead.")
print("As you stand up, you notice two paths ahead — one bathed in sunlight, the other shadowed by dark trees.")
choice1 = input("Do you step onto the SUNLIT path or the SHADOWED path? ").lower()

if choice1 == "sunlit":
    print("\nYou walk toward the warm light. Birds sing above you, but soon you hear rushing water nearby.")
    choice2 = input("Do you follow the SOUND of the river or STAY on the path? ").lower()

    if choice2 == "sound":
        print("\nYou reach a crystal-clear river. Across the water, you spot a cozy cottage.")
        choice3 = input("Do you try to SWIM across or LOOK for a bridge? ").lower()

        if choice3 == "swim":
            print("\nThe water is freezing, but you push through! You make it to the cottage and find a warm fire inside. You survive and live happily ever after! 🏡✨")
        elif choice3 == "look":
            print("\nYou wander too far searching for a bridge and night falls. The forest grows cold and silent... You are lost forever. 🌒")
        else:
            print("\nYou hesitate too long, and something moves in the shadows. You never find out what it is. 💀")

    elif choice2 == "stay":
        print("\nYou continue down the sunny path, but suddenly the ground gives way beneath you!")
        print("You tumble into an underground cavern filled with glowing crystals.")
        choice3 = input("Do you EXPLORE the cave or TRY to climb back up? ").lower()

        if choice3 == "explore":
            print("\nInside the cave, you find ancient treasure! You're rich beyond your dreams! 💎🎉")
        elif choice3 == "try":
            print("\nYou try to climb out, but the walls crumble. You're trapped forever. 😢")
        else:
            print("\nYou sit in the darkness, unsure what to do. Time passes... 🕯️")

    else:
        print("\nYou wander off the path and vanish into the fog. The forest claims another soul. 🌫️")

elif choice1 == "shadowed":
    print("\nYou step into the shadows, where the air feels heavy and cold.")
    print("An eerie silence surrounds you until you spot a flickering lantern on the ground.")
    choice2 = input("Do you PICK up the lantern or LEAVE it alone? ").lower()

    if choice2 == "pick":
        print("\nThe lantern’s light reveals a narrow trail leading deeper into the woods.")
        choice3 = input("Do you FOLLOW the trail or TURN back while you can? ").lower()

        if choice3 == "follow":
            print("\nYou follow the trail to an ancient ruin. Inside, a glowing portal hums with power.")
            print("You step through it... and find yourself in another world. Your adventure begins anew! 🌌✨")
        elif choice3 == "turn":
            print("\nYou try to return, but the path has disappeared. The forest shifts around you... You are never seen again. 🌲💀")
        else:
            print("\nYou stand frozen, the lantern flickering out. Darkness consumes you. 🕯️❌")

    elif choice2 == "leave":
        print("\nYou ignore the lantern and move on. Suddenly, glowing eyes appear in the dark — wolves! 🐺")
        print("You run as fast as you can, but they catch up. The last thing you hear is their howls. 💀")
    else:
        print("\nYou hesitate, and the fog thickens until you can’t breathe. Game over. 🌫️")

else:
    print("\nYou stay still, unsure of what to do, until the mist swallows you whole. 🌀 Game over.")
