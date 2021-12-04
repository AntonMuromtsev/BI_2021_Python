# Instruction

This file was successfully run on Mac OS Catalina (10.15.7, Intel).

Python version : 3.9.1

How to reproduce results:

1) Download pain.py:
wget https://raw.githubusercontent.com/krglkvrmn/Virtual_environment_research/master/pain.py
2) Create dir for file and mv file to it
   mkdir container 
   mv pain.py container
3) Create virtualenv and activate it 
   conda create -n envir python=3.9.1
   conda activate envir
4) Install dependencies from requirments.txt 
   pip install requirments.txt
5) Install certificate for python
    cd /Applications/Python\ 3.9/
    ./Install\ Certificates.command
6) Run the code
   
