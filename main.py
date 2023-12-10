import json
import numpy as np

from data_loader import load_dataset
from commit_analyzer import classify_commit
from project_analyzer import classify_project
from user_analyzer import classify_user

dataset = json.load(open('toy_dataset.json'))
print('The size of dataset:', len(dataset))

# Analyze commits
ave_commit = classify_commit(dataset)
assert ave_commit == 2.0
print('Average number of change per commit:', ave_commit)

# Analyze projects
ave_project = classify_project(dataset)
assert ave_project == 4.0
print('Average number of change per project:', ave_project)

# Analyze users
ave_user = classify_user(dataset)
assert ave_user == 2.0
print('Average number of change per user:', ave_user)