import json
import sys
import os
import pathlib
import re

def get_all_nodes(include, contents):
    pre_nodes = [content["nodes"] for content in contents if (content["id"] == include) & ("nodes" in content)]
    nodes = set()
    nodes.update({node for pre_node in pre_nodes for node in pre_node})
    pre_sub_includes = [content["includes"] for content in contents if (content["id"] == include) & ("includes" in content)]
    sub_includes = set()
    sub_includes.update({include for pre_sub_include in pre_sub_includes for include in pre_sub_include})
    if sub_includes:
        for sub_include in sub_includes:
            nodes.update(get_all_nodes(sub_include, contents))
    return nodes

# filepath = pathlib.Path(sys.argv[1])
filepath = pathlib.Path("E:/学习/Knowledge-Graph/graphs.json")
relationspath = pathlib.Path(os.path.realpath(sys.argv[0])).parent.parent.joinpath("relations.json")
graphspath = pathlib.Path(os.path.realpath(sys.argv[0])).parent.parent.joinpath("graphs.json")

with open(filepath, "r", encoding="utf-8") as file: 
    file_content = json.load(file)
with open(relationspath, "r", encoding="utf-8") as file: 
    relations = json.load(file)
with open(graphspath, "r", encoding="utf-8") as file: 
    graphs = json.load(file)

new_file_content = []

for dic in file_content:
    if ("relations" in dic) & (len(dic["relations"]) == 1) & (dic["relations"][0] == "auto"):
        all_nodes = set()
        if "includes" in dic:
            for include in dic["includes"]:
                all_nodes.update(get_all_nodes(include, graphs))
        if "nodes" in dic:
            all_nodes.update(set(dic["nodes"]))
        all_relations = [relation["id"] for relation in relations if (relation["start"] in all_nodes) & (relation["end"] in all_nodes)]
        dic["relations"] = all_relations
    new_file_content.append(dic)

with open(filepath, "w", encoding="utf-8") as output:
    json.dump(new_file_content, output, indent=4, ensure_ascii=False)