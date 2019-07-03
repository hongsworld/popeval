import os
import json
path = "./IC15/with_dontcare/"
filenames = os.listdir(path)

char_filepaths = sorted([ path + 'img_' + str(x+1).zfill(3) + '.txt' for x in range(500) ])
original_filepaths = sorted([ './word_level-IC15/' + 'img_' + str(x+1).zfill(3) + '.txt' for x in range(500) ])

for origin_path, char_path in zip(original_filepaths, char_filepaths):
    if origin_path.endswith(".txt") and char_path.endswith(".txt"):
        print("=========================")
        print(char_path)
        with open(origin_path) as f:
            content = f.read()
        lines = content.split("\n")
        dont_care_lines = [x for x in lines if x.split(' ')[-1] == "###"]
        content = ""
        try:
            with open(char_path) as f:
                char_content = f.read() 
            if char_content[-1] == "\n":
                char_content = char_content[:-1]
            char_lines = char_content.split("\n")
            
            merged_lines = char_lines + dont_care_lines
            result = "\n".join(merged_lines)
        except:
            print("writing_non_exist_file")
            with open(char_path, 'w') as f:
                f.write('')
            result = "\n".join(dont_care_lines)
            
        with open(char_path, 'w') as f:
            f.write(result)

