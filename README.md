# diffie

# Purpose
  Return differences between two files.

# References

# Results

## run main.py
    cd <project root directory>
    source venv/bin/activate
    python3 diffie/diffie.py

## run unit tests
    cd <project root directory>
    source venv/bin/activate
    python3 diffie/test_diffie.py

---

## Appendix virtual environment venv

The project uses a virtual environment.

https://docs.python.org/3/library/venv.html

This can hold a python version and pip installed packages such as "requests".

https://github.com/kennethreitz/requests

### Install virtual environment in directory named "venv"

    $ cd <project root directory>
    $ pyvenv venv

### Before activating virtual environment

On my machine, active python is 2.7.12

    ➜  diffie git:(master) ✗ which python
    /usr/local/bin/python
    ➜  diffie git:(master) python --version
    Python 2.7.12

On my machine, to use python3 must specify python3

    ➜  diffie git:(master) which python3
    /usr/local/bin/python3

### Activate virtual environment

    ➜  diffie git:(master) source ./venv/bin/activate

### Now active python is in venv and is version 3.5.1

Notice command prompt shows venv is active

    (venv) ➜  diffie git:(master) which python
    /Users/stevebaker/Documents/projects/pythonProjects/diffie/venv/bin/python
    (venv) ➜  diffie git:(master) python --version
    Python 3.5.2

### Deactivate virtual environment
In shell run deactivate
    (venv) ➜  diffie git:(master) ✗ deactivate

## Appendix upgrade pip3
With virtualenv active

    pip3 install --upgrade pip

    Successfully uninstalled pip-8.1.1
    Successfully installed pip-8.1.2

Installed to project venv

