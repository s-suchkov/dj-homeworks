import datetime
import os
from django.http import HttpResponse
from app.settings import FILES_PATH
from django.shortcuts import render
print(os.listdir(FILES_PATH))
print(os.stat(FILES_PATH))


def file_list(request, date=None):
    template_name = 'index.html'
    context = {
        'files': [
        ]
    }
    context_1 = {
        'files': []
    }
    for i in os.listdir(FILES_PATH):
        list = os.path.join(FILES_PATH, i)
        stat = os.stat(list)
        file = {'name': i,
         'ctime': datetime.datetime.fromtimestamp(stat.st_ctime),
         'mtime': datetime.datetime.fromtimestamp(stat.st_mtime)}
        context['files'].append(file)
        if date!= None:
            date_res = file['mtime'].date()
            if str(date) == str(date_res):
                context_1['files'].append(file)
    if date != None:
        context_1['date'] = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        return render(request, template_name, context_1)

    return render(request, template_name, context)

def file_content(request, name):
    server = os.path.join(FILES_PATH, name)
    if os.path.exists(server):
        with open(server, 'r') as file:
            content = file.read()
        return render(
            request,
            'file_content.html',
            context={'file_name': name, 'file_content': content}
        )
    else:
        return render(
            request,
            'file_content.html',
            context={'file_name': 'нет файла', 'file_content': ''}
        )

