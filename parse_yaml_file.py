import yaml
import os

a_yaml_file = open("example.yaml")

parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)

lst = parsed_yaml_file.get("steps")

dct = lst[0]

print(dct)

x = dct.get("command")

print(x)

for item in x:
    print(item)
    # os.system(item)
    stream = os.popen(item)
    print(stream.read())



