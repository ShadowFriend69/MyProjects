PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

