import csv
from .models import Path_csv, Fields
from django.shortcuts import render
import os
if len(Path_csv.objects.all())==0:
    Path_csv.objects.create(file=os.path.abspath("phones.csv"))
# CSV_FILENAME = 'phones.csv'
# COLUMNS = [
#     {'name': 'id', 'width': 1},
#     {'name': 'name', 'width': 3},
#     {'name': 'price', 'width': 2},
#     {'name': 'release_date', 'width': 2},
#     {'name': 'lte_exists', 'width': 1},
# ]


def table_view(request):
    CSV_FILENAME = Path_csv.objects.all()[0].file
    COLUMNS = Fields.objects.all().order_by('id')
    template = 'table.html'
    with open(f'{CSV_FILENAME}', 'rt') as csv_file:
        header = []
        table = []
        table_reader = csv.reader(csv_file, delimiter=';')
        for table_row in table_reader:
            if not header:
                header = {idx: value for idx, value in enumerate(table_row)}
            else:
                row = {header.get(idx) or 'col{:03d}'.format(idx): value
                       for idx, value in enumerate(table_row)}
                table.append(row)

        context = {
            'columns': COLUMNS,
            'table': table,
            'csv_file': CSV_FILENAME
        }
        result = render(request, template, context)
    return result
