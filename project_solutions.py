# solutions below are based in part on:
# wget http://jarrodmillman.com/capstone/code/senators.py
# wget http://jarrodmillman.com/capstone/code/senators2.py

import json
from operator import itemgetter
import re
import numpy as np
import pandas as pd

# 1. Load the *senators-list.json* and *timelines.json* files as objects called *senators* and *timelines*.

# using 'with' here closes the file automatically
import os
os.chdir('project')  # if needed 

with open("senators-list.json") as f:
    senators = json.load(f)

with open("timelines.json") as f:
    timelines = json.load(f)

# 2. What type of datastructure is *timelines*? How many timelines are there? What does each timeline correspond to?

type(timelines)
type(timelines[0])
type(timelines[0][0])

len(timelines)  # 100 senators
len(timelines[0]) # 200 tweets
timelines[0][0]

timelines[0][0].keys()
timelines[0][0]["text"]

timelines[0][0]["user"].keys()
timelines[0][0]["user"]['screen_name']
timelines[0][0]["user"]["followers_count"]

# 3. Make a list of the number of followers each senator has.

len(senators)
senators.keys()
len(senators['users'])
senators['users'][0].keys()

popularity = [(s['name'], s['followers_count']) for s in senators['users']]


