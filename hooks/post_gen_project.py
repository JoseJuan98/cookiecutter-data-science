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
        os.remove(path=filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(path=filepath)


if "{{cookiecutter.project_kind}}" == "python library":
    # User does not want folder so remove it
    for folder in os.listdir(src_path):
        if folder not in ["{{ cookiecutter.project_name }}", "__init__.py", "py.typed"]:
            remove(os.path.join(src_path, folder))

    for file in ["test.txt", "analysis.txt"]:
        remove(os.path.join(parent_path, "requirements", file))

    for folder in ["artifacts", "notebooks", "reports"]:
        remove(os.path.join(parent_path, folder))

else:
    remove(os.path.join(src_path, "{{ cookiecutter.project_name }}"))
    remove(os.path.join(src_path, "py.typed"))
    remove(os.path.join(parent_path, "setup.py"))
