import json
import sys
import os
import pathlib
import re

filepath = pathlib.Path(sys.argv[1])
nodespath = pathlib.Path(os.path.realpath(sys.argv[0])).parent.parent.joinpath("nodes.json")
relationspath = pathlib.Path(os.path.realpath(sys.argv[0])).parent.parent.joinpath("relations.json")
includespath = pathlib.Path(os.path.realpath(sys.argv[0])).parent.parent.joinpath("graphs.json")

with open(filepath, "r", encoding="utf-8") as file: 
    file_content = json.load(file)
with open(nodespath, "r", encoding="utf-8") as file: 
    nodes = json.load(file)
with open(relationspath, "r", encoding="utf-8") as file: 
    relations = json.load(file)
with open(includespath, "r", encoding="utf-8") as file: 
    includes = json.load(file)

    
new_file_content = []
for dic in file_content:
    node_res = []
    relations_res = []
    include_res = []
    if "nodes" in dic:
        node_res = dic["nodes"]
    if "relations" in dic:
        relation_res = dic["relations"]
    if "includes" in dic:
        include_res = dic["includes"]
    new_nodes = set()
    new_relations = set()
    new_includes = set()
    for node_re in node_res:
        if node_re.startswith("re::"):
            patten = re.compile(node_re[4:])
            new_nodes.update({node["id"] for node in nodes if patten.match(node["id"])})
        else:
            new_nodes.add(node_re)
    for relation_re in relation_res:
        if relation_re.startswith("re::"):
            patten = re.compile(relation_re[4:])
            new_relations.update({relation["id"] for relation in relations if patten.match(relation["id"])})
        else:
            new_relations.add(relation_re)
    for include_re in include_res:
        if include_re.startswith("re::"):
            patten = re.compile(include_re[4:])
            new_includes.update({include["id"] for include in includes if patten.match(include["id"])})
        else:
            new_includes.add(include_re)
    if "nodes" in dic:
        dic["nodes"] = list(new_nodes)
    if "relations" in dic:
        dic["relations"] = list(new_relations)
    if "includes" in dic:
        dic["includes"] = list(new_includes)

    new_file_content.append(dic)

with open(filepath, "w", encoding="utf-8") as output:
    json.dump(new_file_content, output, indent=4, ensure_ascii=False)