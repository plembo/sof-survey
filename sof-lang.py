# Show 5 most popular languages
import csv
from collections import Counter

with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    total = 0

    language_counter = Counter()

    for line in csv_reader:
        languages = line['LanguageWorkedWith'].split(';')

        language_counter.update(languages)

        total += 1

for language, value in language_counter.most_common(5):
    language_pct = (value / total) * 100
    language_pct = round(language_pct, 2)

    print(f'{language}: {language_pct}%')
