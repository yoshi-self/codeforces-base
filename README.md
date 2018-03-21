My working directory of Codeforces

## Features
* Create a directory for a problem
* Retrieve input & output examples from the problem page
* Test input & output with cftest.py

## Installation
Clone this repository and rename the directory as you like

## Usage
NOTE: The term "Problem ID" refers [ContestID + ProblemIndex] like "50A"

### 1. Create problem directory
```
# by specifying problem ID
./cfprepare.py 50A
```
or
```
# by specifying problem URL
./cfprepare.py http://codeforces.com/problemset/problem/50/A
```

A directory named [ProblemID] will be created, which contains
* [ProblemID].cpp
  * Copy of main.cpp
* build.sh
  * Shell script to compile the source with ../g++cf
* cftest.py
  * Python script to test the program with input & output examples
* test.txt
  * input & output examples retrieved from Codeforces page
  
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

## Syntax of test.txt
It's just a xml-like sequence of input and output
```
<input>
1st input
</input>
<output>
expected output for 1st input
</output>
<input>
2nd input
</input>
<output>
expected output for 2nd input
</output>
<input>
In case you don't want to test, just check output
</input>
<output>
<nooutput />
</output>
```
