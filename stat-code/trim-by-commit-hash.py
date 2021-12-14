import csv

results = {}
count = 0
output = []
with open('tmp-results.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(row['actions repository'], row['commit hash'])
        commit = row['commit hash']
        analyzed = row['status'] == '1' or row['status'] == '0'
        if commit in results:
            if not analyzed:
                row['status'] = results[commit]
                row['responsible'] = 'python'
                count += 1
        elif analyzed:
            if commit not in results:
                results[commit] = row['status']
        
        print(row['actions repository'], row['commit hash'], row['commit date'], row['commit url'],row['responsible'], row['status'], row['comments'], sep=',')


print(count)