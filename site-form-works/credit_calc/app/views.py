
from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"


    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            initial_fee = form.cleaned_data['initial_fee']
            rate = form.cleaned_data['rate']
            months_count = form.cleaned_data['months_count']
            common_result = initial_fee + initial_fee * rate / 100
            result = round(common_result / months_count, 2)
            print(form)
            context = {
                'form': form,
                'common_result': common_result,
                'result': result
            }
    else:
        form = CalcForm()
        context = {
            'form': form
        }
    return render(request, template, context)

# form = CalcForm.objects.all()
# print(form)