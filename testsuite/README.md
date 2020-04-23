# The Profiles Vocabulary - Test Suite
This repository contains a test suite - software - for testing the validity of claimed implementations of 
[The Profiles Vocabulary (PROF)](https://w3c.github.io/dxwg/prof/). 

## How the Test Suite Works
This test suite uses the [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) to describe
necessary *graph shapes* for expected to be found in PROF implementations. These *Shapes* are given in a
series of *Shapes files* within the [shapes](shapes/) folder of this repository and are applied to target
data (implementations) using the [pySHACL](https://pypi.org/project/pySHACL/) open source SHACL validation
tool.

## Running the Test Suite
The file [run.py](run.py) contains a Python script that runs pySHACL against a series of listed PROF 
implementations. In some cases, the implementations are not able to be validated without preprocessing, 
e.g. where the implementation is a PROF template that must be instantiated to be used. 
 
The system requirements to execute the *run.py* file are:
 
* Python 3 (3.5+) 
* Python modules as listed in [requirements.txt](requirements.txt)
* a working Internet connection (to retrieve remote resources)
 
With those satisfied, the script can be run, as per any normal Python command line script.

## Results
When run, the test suite produces a CSV file of Implementation Results, reflecting Table 1 in the 
[PROF Implementation Report's *results* section](https://w3c.github.io/dxwg/prof-implementation-report/#implementations) 
with the addition of a Pass/Fail column indicating whether or not the implementation passed all SHACL 
tests.

Note that this Test Suite does *not* present implementation results per PROF element. 