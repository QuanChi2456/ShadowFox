total_jumping_jacks = 100
jumping_jacks_per_set = 10
completed = 0

for i in range(0, total_jumping_jacks, jumping_jacks_per_set):
    completed += jumping_jacks_per_set
    print(f"You did {jumping_jacks_per_set} jumping jacks.")
    
    if completed >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        else:
            print(f"{total_jumping_jacks - completed} jumping jacks remaining.")
    elif tired in ['no', 'n']:
        print(f"{total_jumping_jacks - completed} jumping jacks remaining.")
