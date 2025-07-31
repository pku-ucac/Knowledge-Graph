import json
import sys
import os
import pathlib

input_path = pathlib.Path(sys.argv[1])
current_path = pathlib.Path(os.getcwd())
id_prefix = input_path.name.split('#')[0]

output_filename = "output.json"
if len(sys.argv) > 2:
    output_filename = "output_{}.json".format(sys.argv[2])

filenames = [file.name for file in input_path.iterdir() if file.is_file() & file.name.count('#')==1]
ids_names = list(map(lambda s: s.split('#'), filenames))
ids, names = tuple(map(list, zip(*ids_names)))
result = [{"id":"n"+id_prefix+"/"+id, "name":name, "type":"node", "path":input_path.joinpath(filename).as_posix()} for id, name, filename in zip(ids, names, filenames)]

with open(current_path.joinpath(output_filename), "w", encoding="utf-8") as output:
    json.dump(result, output, indent=4, ensure_ascii=False)