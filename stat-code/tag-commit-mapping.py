import os
import subprocess
from os import path
import csv
import json

ROOT = '/mnt/drive/actions-repos'
vulnCommits = {}

with open('vulnerable-actions-commits.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['status'] == '1':
            repo = row['repo'].lower() 
            dir = repo.replace('/', '#')
            if repo not in vulnCommits:
                vulnCommits[repo] = {'seed': row['commit']}


for k, v in vulnCommits.items():
    print(k, v)
    dir = k.replace('/', '#')
    os.chdir(f'{ROOT}/{dir}')
    # output = subprocess.check_output([f'git log --pretty=%P {v["seed"]}'])
    output = subprocess.check_output(['git', 'log', '--pretty=%P', v["seed"]]).decode()
    commits = output.splitlines(keepends=False)
    output = subprocess.check_output(['git', 'tag', '--no-contains',v["seed"]]).decode()
    tags = output.splitlines(keepends=False)
    commits.extend(tags)
    v['refs'] = commits

with open('mapped-vulnerable-commits.json', 'w') as f:
    json.dump(vulnCommits, f)
