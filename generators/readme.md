register_node用法：
python.exe register_node.py folder [name]
这将创建一个名为output_name.json的文件，包含所有的nodes

replace_re_for_node用法：
python.exe replace_re_for_node.py file
替换file中关于node的正则表达式，参见graphs_example.json

generate_relations用法：
python.exe replacgenerate_relations.py file
在替换完node后，自动生成所有与这些node相关的relations，参见graphs_example.json