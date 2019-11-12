import csv
from collections import defaultdict, Counter

with open('survey_results_public.csv', encoding='utf-8') as f:
    csv_reader = csv.DictReader(f)
    dev_type_info = {}

    for line in csv_reader:
        dev_types = line['DevType'].split(';')

        for dev_type in dev_types:
            if not dev_type == 'NA':  # filter dev_type that respondant didn't answered
                dev_type_info.setdefault(dev_type, {
                    'total': 0,
                    'language_counter': Counter()
                })

                languages = line['LanguageWorkedWith'].split(';')
                dev_type_info[dev_type]['language_counter'].update(languages)
                dev_type_info[dev_type]['total'] += 1

for dev_type, info in dev_type_info.items():
    print(dev_type)

    for language, value in info['language_counter'].most_common(5):
        language_pct = (value / info['total']) * 100
        language_pct = round(language_pct, 2)

        print(f"\t{language}: {language_pct}%")

    # total = 0

    # yes_count = 0
    # no_count = 0

    # counts = defaultdict(int)
    # counts = Counter()
    # language_counter = Counter()

    # for line in csv_reader:
    #     if line['Hobbyist'] == 'Yes':
    #         yes_count += 1
    #     elif line['Hobbyist'] == 'No':
    #         no_count += 1

        # for dev_type in dev_types:
        #     dev_type_info[dev_type] = {}

    # language_counter[line['LanguageWorkedWith']] += 1
#         languages = line['LanguageWorkedWith'].split(';')
#         language_counter.update(languages)
#         total += 1

#         # for language in languages:
#         #     language_counter[language] += 1


# # print(language_counter.most_common(5))
# for language, value in language_counter.most_common(5):
#     language_pct = value / total * 100
#     language_pct = round(language_pct, 2)

#     print(f"{language}: {language_pct}%")

#         counts[line['Hobbyist']] += 1

# total = counts['Yes'] + counts['No']

# yes_pct = counts['Yes'] / total * 100
# yes_pct = round(yes_pct, 2)

# no_pct = counts['No'] / total * 100
# no_pct = round(no_pct, 2)

# print(f"Yes: {yes_pct}%")
# print(f"No: {no_pct}%")
