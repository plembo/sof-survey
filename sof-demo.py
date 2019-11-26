import csv


with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    for line in csv_reader:
        print(line['Hobbyist'])
