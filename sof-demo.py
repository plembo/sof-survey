import csv


with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    counts = {
        'Yes': 0,
        'No': 0
    }

    for line in csv_reader:
        counts[line['Hobbyist']] += 1

total = counts['Yes'] + counts['No']

yes_pct = (counts['Yes'] / total) * 100
yes_pct = round(yes_pct, 2)
no_pct = (counts['No'] / total) * 100
no_pct = round(no_pct, 2)

print(f'Yes: {yes_pct}%')
print(f'No: {no_pct}%')
