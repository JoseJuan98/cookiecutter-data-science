import os
import shutil

from pathlib import Path

# Current path
path = Path(os.getcwd())

# Source path
parent_path = os.path.join(path.parent.absolute(), "{{ cookiecutter.repo_name }}")
src_path = os.path.join(parent_path, "src")


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.project_kind}}" == "python library":
    # User does not want folder so remove it
    [remove(folder) for
     folder in os.listdir(src_path)
     if folder not in ["{{ cookiecutter.project_name }}", "__init__.py", "py.typed"]
     ]
    remove(os.path.join(parent_path, "requirements", "test.txt"))
    remove(os.path.join(parent_path, "requirements", "analysis.txt"))

else:
    remove(os.path.join(src_path, "{{ cookiecutter.project_name }}"))
    remove(os.path.join(src_path, "py.typed"))
    remove(os.path.join(parent_path, "setup.py"))
