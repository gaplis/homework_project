from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .forms import ChangeProductForm, ImageForm
from homework_2_app.models import Product


# Create your views here.
def update_product(request):
    if request.method == 'POST':
        form = ChangeProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            pk = form.cleaned_data['pk']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            product = Product.objects.filter(pk=pk).first()
            product.name = name
            product.description = description
            product.price = price
            product.count = count
            product.save()
            message = f'Данные продукта {product.pk} обновлены'
    else:
        form = ChangeProductForm()
        message = 'Заполните форму'
    return render(request, 'homework_4_app/update_product.html', {'form': form, 'message': message})


def upload_image_product(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            pk = form.cleaned_data['pk']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            product = Product.objects.filter(pk=pk).first()
            product.image = image
            product.save()
            message = f'Добавлена картинка продукта {product.pk}'
    else:
        form = ImageForm()
        message = 'Выберите картинку продукта'
    return render(request, 'homework_4_app/upload_image_product.html', {'form': form, 'message': message})
