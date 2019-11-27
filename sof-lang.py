import csv
from collections import Counter

with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    language_counter = Counter()

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')

        language_counter.update(languages)

print(language_counter)

#       counts[line['Hobbyist']] += 1

# total = counts['Yes'] + counts['No']

# yes_pct = (counts['Yes'] / total) * 100
# yes_pct = round(yes_pct, 2)
# no_pct = (counts['No'] / total) * 100
# no_pct = round(no_pct, 2)

# print(f'Yes: {yes_pct}%')
# print(f'No: {no_pct}%')
