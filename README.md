My working directory of Codeforces

## Features
* Create a directory for a problem
* Reetrieve input & output examples from the problem page
* Test input & output with cftest.py

## Installation
Clone this repository and rename the directory as you like

## Usage
NOTE: Term "Problem ID" refers [ContestID + ProblemIndex] like "50A"

### 1. Create problem directory
```
# by specify problem ID
./cfprepare.py 50A
```
or
```
# by specify problem URL
./cfprepare.py http://codeforces.com/problemset/problem/50/A
```

A directory named [ProblemID] will be created, which contains
* [ProblemID].cpp
  * Copy of main.cpp
* build.sh : do 
  * Shell script to compile source with ../g++cf
* cftest.py
  * Python script to test the program with example inputs & outputs
* test.txt
  * example input & output pairs retrieved from Codeforces page
  
### 2. Write code
Modify [ProblemID].cpp

### 3. build
```
./build
```

### 4. Test
```
./cftest.py
```
With -b option, it builds before test.
