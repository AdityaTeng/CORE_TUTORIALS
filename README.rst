Project setup
Link: https://www.youtube.com/watch?v=DaxcmbWcdTA&t=5350s

Continue at Tutorial 3: Logging
=============

Project setup instructions here.

mkdir -p local
cp core/project/settings/templates/settings.dev.py ./local/settings.dev.py

venv commands:
source venv/bin/activate
deactivate

pre-commit commands:
poetry run pre-commit install
poetry run pre-commit run --all-files

# NOTE:
Having issues with pre-commit.yaml file
[isort and flake8]
