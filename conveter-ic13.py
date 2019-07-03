import os
import json
path = "./IC13/"
filenames = os.listdir(path)
print(filenames)
print(len(filenames))

filepaths = sorted([ path + x for x in filenames])

for path in filepaths:
    result = ""
    if path.endswith(".json"):
        print("=========================")
        print(path)
        with open(path) as f:
            parsed_json = json.loads(f.read())
        content = ""
        for polygon in parsed_json['shapes']:
            line = ""
            for point in polygon['points']:
                line += str(point[0]) + " " + str(point[1]) + " "
            line += polygon['label']
            content += line + "\n" 
            if len(polygon['points']) != 4:
                print(len(polygon['points']))
                assert False
        with open(path[:-5] + "_char.txt", 'w') as f:
            f.write(content)

