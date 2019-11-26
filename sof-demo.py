import csv


with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    yes_count = 0
    no_count = 0

    for line in csv_reader:
        if line['Hobbyist'] == 'Yes':
            yes_count += 1
        elif line['Hobbyist'] == 'No':
            no_count += 1

total = yes_count + no_count

print(yes_count / total)
print(no_count /total)
