with open("books/frankenstein.txt") as f:
    if '/' in f.name:
        filename_index = f.name.rfind('/')
    elif '\\' in f.name:
        filename_index = f.name.rfind('\\')
    else:
        filename_index = -1
    print(f"------ Statistics for {f.name[filename_index+1:]} ------")
    text_contents = f.read()
    word_list = text_contents.split()
    print(f"{len(word_list)} words in the file.\n")

    character_dict = {}
    text_string = str(text_contents)
    for s in text_string.lower():
        if s in character_dict:
            character_dict[s] += 1
        else:
            character_dict[s] = 1
    character_list = list(character_dict.values())
    sorted_character_values = sorted(character_list, reverse=True)
    sorted_character_dict = {key: value for value in sorted_character_values 
                             for key, v in character_dict.items() if v == value}

    for char in sorted_character_dict:
        if char.isalpha():
            print(f"The {char} character was found {sorted_character_dict[char]} times.")
    print("------ End of statistics ------")
