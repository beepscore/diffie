# diffie

# Purpose
Return differences between two files.

# References

## searcher
https://github.com/beepscore/searcher.git

# Results

## input
In data/input put one or more pairs of similarly named files to diff.
App will diff files whose names differ by an ending "c". e.g. "a.txt": "ac.txt"

## output
App writes results to data/output/results.txt

## run main.py
### macOS
    cd <project root directory>
    source venv/bin/activate
    python3 -m main

### Windows
    cd <project root directory>
    venv\Scripts\activate.bat
    python3 main.py

## Unit tests
To run tests, open terminal shell.  
cd to project directory. Run tests via python command or bash script.
    cd <project root directory>
    
### python command
This command lists and tests all modules

    python3 -m unittest discover -s tests/

Alternatively, can supply test module names as args

    python3 -m unittest tests.test_diffie tests.test_file_writer
    
### Bash script
Runs all test modules.  
Works on macOS. On Windows may work with Cygwin, I don't know.

    cd <project root directory>
    source venv/bin/activate
    bin/run_tests

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

