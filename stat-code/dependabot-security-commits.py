from sys import argv, exit, stderr
import os
import json
import re

if len(argv) != 2:
    print(f'Usage: {argv[0]} DIRECTORY (where results of git-vuln-finder are stored)', file=stderr)
    exit(1)

ROOT=argv[1]
os.chdir(ROOT)


for file in os.listdir(ROOT):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            data = json.load(f)
            for commit, value in data.items():
                origin = value['origin'].replace('.git', '')
                repo = origin.replace('https://github.com/', '')
                depbump = ''
                if value['author'] == 'dependabot-preview[bot]' and re.search('[Security]', value['message']):
                    depbump = 'dependency bump'
                print(','.join([repo, commit, str(value['committed_date']), f'{origin}/commits/{commit}', depbump]))

            # exit(0)

