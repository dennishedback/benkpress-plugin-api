# newton
Template repository for new python projects.

## Initialization checklist
To initialize template for use in a new project, do the following:

1. Choose a license by renaming one of the licensing options to "LICENSE" and delete all other options.
2. Rename one of the dunder init options under package/ to dunder init according to your licensing choice. Delete the others.
3. If using GPL, edit the information about the program in dunder init file (use same description on github, first line of README, and in setup.py)
4. Rename the folder "package" to the name of your actual main module.
5. `virtualenv venv && ./venv/bin/activate`
6. `(venv) pip install -r requirements-dev.txt`
7. `(venv) pip freeze > requirements-dev.txt`
8. Change revision of formatters in .pre-commit-config.yaml to match revision in requirements-dev.txt
9. `(venv) pre-commit install`
10. Edit tox.ini to match your python versions, and rename the line `mypy package` to match the name of your package.
11. Edit setup.py
12. Clear all text in this README and write a new README for the project.
