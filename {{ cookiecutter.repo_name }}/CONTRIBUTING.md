# Contributing

## Set up your dev env

* install virtualenv and virtualenvwrapper globally
* do anything you want to your .zshrc for virtualenv (readthedocs)
* create a virtualenv using the latest stable python.
* enable the virtual env
* install the package deps in dependencies

```
❯ pip install virtualenv 

# this is for when you need to make the virtualenv
❯ python -m virtualenv venv --python=<path_to_python>  # in windows e.g. 'C:\Program Files\Python311\python.exe'
                                                       #            notice that single quotes are needed
                                                       # in Linux e.g. /usr/bin/python
# activate the virtualenv
# In Windows
❯ .\venv\Scripts\activate
# In Linux
❯ source ./venv/bin/activate 

# Update pip
❯ python -m pip install -U pip setuptools<=67.0.0 wheel build

# now that we're in our virtualenv, use the virtualenv pip to install the required packages
❯ pip install -e .

# but wait! we want to be able to run tests, so go ahead and install the test dependencies too
❯ pip install -e .[dev,test]
```

so after this, your virtualenv is ready to do all the fun stuff in a safe way

## Running basic script

Let's execute the command line script to get a pipeline definition from one of the pipeline scripts in the project.

```
# activate the virtualenv
# In Windows
❯ .\venv\Scripts\activate
# In Linux
❯ source ./venv/bin/activate 

❯ get-pipeline-definition --help
usage: Gets the pipeline definition for the pipeline script. [-h] [-n MODULE_NAME] [-kwargs KWARGS]

optional arguments:
  -h, --help            show this help message and exit
  -n MODULE_NAME, --module-name MODULE_NAME
                        The module name of the pipeline to import.
  -kwargs KWARGS, --kwargs KWARGS
                        Dict string of keyword arguments for the pipeline generation (if supported)
```

## Running tests locally in your development virtual environment

Start up your virtualenv again and let's get to testing

```
# activate the virtualenv
# In Windows
❯ .\venv\Scripts\activate
# In Linux
❯ source ./venv/bin/activate 

❯ python -m pytest   
============================================================= test session starts =============================================================
cachedir: .pytest_cache
plugins: cov-2.10.1
collected 1 items                                                                                                                               

test/integration/test_pipelines.py::test_pipelines                    PASSED                                                                          [100%]

======================================================== 1 passed, 1 xfailed in 0.04s =========================================================
```

There you go, have fun developing!

## Running Tests in isolated environments with Tox

`tox` is a great python tool to run tests in isolated environments with different python versions
and more.

Before any test, first activate your virtualenv and install tox if it wasn't installed already:
```
# activate the virtualenv
# In Windows
❯ .\venv\Scripts\activate
# In Linux
❯ source ./venv/bin/activate

pip install tox
``` 

Then to run tests, simply run the following command from the root directory of the repository:

```shell
python -m tox -e py310
```

This command will create a virtual environment for each environment specified in the envlist of the tox.ini file. The test environment will run the test suite, while the flake8 and mypy environments will check for code quality.

If you are using Windows, try `python -m tox` instead of only tox.

You can also pass additional arguments to the pytest command by appending them to the tox command. For example, to run tests and show the output of print statements, run:

```shell
python -m tox -- -s
```

### Ignoring Coverage Checks

By default, the test environment will fail if the code coverage is less than 90%. You can ignore this check by setting the IGNORE_COVERAGE environment variable to -. For example:

```bash
export IGNORE_COVERAGE=- ; python -m tox -e py310 ; unset IGNORE_COVERAGE
```

## Building and Distributing Packages

To build and check the distribution packages, use the twine environment:

```bash
python -m tox -e twine
```

This command will build a wheel file and check the package's README for valid reStructuredText markup.

## Cleaning Up

To erase all previous coverage data, run:

```
python -m tox -e clean
```

This will remove all previous coverage data and test results.

## Reporting

To generate a coverage report, run:

```
python -m tox -e report
```

This will generate a coverage report based on the most recent test run.


