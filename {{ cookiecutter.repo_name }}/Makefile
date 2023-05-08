.PHONY: requirements data lint environment clean_environment clean test dev_requirements

# _________________________ GLOBALS _________________________

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
PACKAGE_MANAGER = {{ cookiecutter.package_manager }}
PYTHON_VERSION = {{ cookiecutter.python_version }}

# _________________________ COMMANDS _________________________

# In case a command need args
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

# to use args
# $(call args, <default_value>)

## Create python virtual environment.
{%- if cookiecutter.package_manager == "pip" -%}
## By default uses /usr/bin/python{{ cookiecutter.python_version }} as python dir, change python version by passing an argument e.g. `make create_env /usr/bin/python3.10`
{% endif %}
environment:
ifneq (,$(wildcard ./venv))
	@echo The virtual environment has been already created;
else
ifeq ($(PACKAGE_MANAGER),"conda")
	@echo ">>> Detected conda, creating conda environment."
	conda create --name $(PROJECT_NAME) python=$(PYTHON_VERSION)
	@echo ">>> New conda env created. Activate with:\nsource activate $(PROJECT_NAME)"
else
	@echo Creating venv venv;
	$(PYTHON_INTERPRETER) -m pip install -U pip virtualenv;
	$(PYTHON_INTERPRETER) -m virtualenv venv;

	$(PYTHON_INTERPRETER) -m pip install --no-cache-dir -U pip setuptools wheel build virtualenv
	$(PYTHON_INTERPRETER) -m virtualenv --python=$(call args, "/usr/bin/python{{ cookiecutter.python_version }}") venv
endif
endif

## Clean virtual environment
environment_clean:
ifneq (,$(wildcard ./venv))
	deactivate || echo "Already venv deactivated";
	rm -rf venv;
	find . -type d -name "{{ cookiecutter.project_name }}.egg-info" -exec rm -rf {} \; || echo 'Already dirs';
	rm -rf build/ || echo 'Already deleted build/';
else
	@echo It has been cleaned already
endif

## Install Python Dependencies for development
requirements:
ifneq (,$(wildcard ./venv))
	@bash -c "source ./venv/bin/activate"
	$(PYTHON_INTERPRETER) -m pip install --no-cache-dir -U pip setuptools wheel build
	$(PYTHON_INTERPRETER) -m pip install --no-cache-dir -U {%- if cookiecutter.project_kind == "data science" -%} -r requirements/core.txt {%- elif cookiecutter.project_kind == "python library" -%} -e .[build,test,dev] {% endif %}
else
	@echo The virtualenv must be created first. Please use "make create_env"
endif

{%- if cookiecutter.project_kind == "data science" -%}
## Install dependencies for testing
dev_requirements:
	$(PYTHON_INTERPRETER) -m pip install --no-cache-dir -r requirements/test.txt

## Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) src/data/make_dataset.py data/raw data/processed
{% endif %}

## Lint using flake8
lint:
	python -m tox -p -e flake8,mypy

## Test using pytest and coverage
cov-test:
	$(PYTHON_INTERPRETER) -m tox -e py311

## Display coverage report
report:
	$(PYTHON_INTERPRETER) -m tox -e report

## Delete all compiled Python files
clean:
	find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf || echo 'Already clean dirs'
	$(PYTHON_INTERPRETER) -m tox -e clean


# _________________________ Self Documenting Commands _________________________

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
