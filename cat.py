import json
import sys

# handle argument exceptions
if len(sys.argv) < 3:
    raise Exception('参数数量必须大于 2！')


# accept argument list
notebook_path_lst = sys.argv[1:]

target_notebook = {}
cells_lst = []

# read notebook path list
for path in notebook_path_lst:
    with open(path) as notebook:
        
        if( path.split('.')[-1] != 'ipynb' ):
            raise Exception('参数必须是ipynb类型的文件')
        
        notebook_str = notebook.read()
        notebook_json = json.loads(notebook_str)
        cells = notebook_json['cells']
        cells_lst += cells

target_notebook['cells'] = cells_lst

with open(notebook_path_lst[0]) as notebook:
    notebook_str = notebook.read()
    notebook_json = json.loads(notebook_str)

del notebook_json['cells']
target_notebook.update(notebook_json)
target_str = json.dumps(target_notebook)

with open('target_notebook.ipynb', 'w') as target:
    target.write(target_str)

