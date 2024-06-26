import os
import shutil

from pathlib import Path

# Current path
path = Path(os.getcwd())

# Source path
parent_path = os.path.join(path.parent.absolute(), "{{ cookiecutter.repo_name }}")


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(path=filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(path=filepath)


if "{{cookiecutter.project_kind}}" == "python library":
    # User does not want folder so remove it
    remove(os.path.join(parent_path, "pipeline"))

    for file in ["test.txt", "analysis.txt"]:
        remove(os.path.join(parent_path, "requirements", file))

    for folder in ["artifacts", "notebooks", "reports"]:
        remove(os.path.join(parent_path, folder))

    remove(os.path.join(parent_path, "src", "{{ cookiecutter.project_name }}", "visualization"))
    remove(os.path.join(parent_path, "src", "paths.py"))

else:
    # Rename the folder to common
    os.rename(
        os.path.join(parent_path, "{{ cookiecutter.project_name }}"),
        os.path.join(parent_path, "common"),
    )
