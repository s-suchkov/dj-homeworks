from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View
from .models import Product, Review
from .forms import ReviewForm
from django.http import HttpResponse

def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


# def product_view(request, pk):
#     template = 'app/product_detail.html'
#     product = get_object_or_404(Product, id=pk)
#
#     form = ReviewForm
#     if request.method == 'POST':
#         # логика для добавления отзыва
#         pass
#
#     context = {
#         'form': form,
#         'product': product
#     }
#
#     return render(request, template, context)

class MyForm(View):
    form_class = ReviewForm
    template = 'app/product_detail.html'
    def get(self, request, pk):
        id = []
        product = get_object_or_404(Product, id=pk)
        id.append(pk)
        if pk in id:
            context = {
                'product': product,
                'reviews': product.review_set.all(),
                'is_review_exist': True
            }
        else:
            context = {
                'form': self.form_class,
                'product': product,
                'reviews': product.review_set.all()
            }
        return render(request, self.template, context)

    def post(self, request, pk):
        id = []
        form = self.form_class(request.POST)
        product = get_object_or_404(Product, id=pk)

        request.session['id'] = id

        if form.is_valid() and not(pk in request.session['id']):

            reviews = product.review_set.create(text=form.cleaned_data['text'])
            request.session['text'] = form.cleaned_data['text']
            id.append(pk)
            request.session['s_review_exist'] = True
            context = {
            'reviews': product.review_set.all(),
            'product': product,
            'is_review_exist': request.session['s_review_exist']
            }
        else:
            context = {
                'reviews': product.review_set.all(),
                'product': product,
                'is_review_exist': request.session['s_review_exist']
            }
        return render(request, self.template, context)