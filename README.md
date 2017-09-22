# diffie

# Purpose
Python project to return differences between two files.

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
cd to project directory. Run tests via command line or PyCharm test configuration.
    cd <project root directory>
    
### command line
#### python command
This command lists and tests all modules

    python3 -m unittest discover

Alternatively, can supply test module names as args

    python3 -m unittest tests.test_diffie tests.test_file_writer
    
#### Bash script
Runs all test modules.  
Works on macOS. On Windows may work with Cygwin, I don't know.

    cd <project root directory>
    source venv/bin/activate
    bin/run_tests

### PyCharm test configuration
.idea files aren't in source control, so describe configuration setup here.
Add from Defaults/Python tests/unittests

#### Target / Path

    tests/

#### pattern
can leave this blank

#### Python interpreter
Python 3.6.1 (~/anaconda/envs/beepscore/bin/python)

#### Working directory
Setting this fixes "no such file or directory error" when running tests in this project.
Many projects don't need this setting.

    .../diffie
    
select add content roots to python path
select add source roots to python path

## Appendix Anaconda

The project uses an Anaconda environment.

### Activate anaconda environment

    beepscore02:diffie stevebaker$ source activate beepscore

Notice command prompt shows anaconda environment is active

    (beepscore) beepscore02:diffie stevebaker$

    (beepscore) beepscore02:diffie stevebaker$ which python
    /Users/stevebaker/anaconda/envs/beepscore/bin/python

    (beepscore) beepscore02:diffie stevebaker$ python --version
    Python 3.6.2 :: Continuum Analytics, Inc.


### Deactivate virtual environment
In shell run source deactivate

    (beepscore) beepscore02:diffie stevebaker$ source deactivate
