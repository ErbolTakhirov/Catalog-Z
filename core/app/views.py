# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Object, Category
# from .forms import ObjectCreateForm, ObjectUpdateForm
#
#
# def index_view(request):
#     obj = Object.objects.all()
#
#     return render(request, 'app/index.html', context={'obj': obj})
#
#
# # def Object_detail(request, pk):
# #     object = Object.objects.get(id=pk)
# #
# #     if request.method == 'POST':
# #         form = ObjectUpdateForm(request.POST, instance=object)
# #
# #         if form.is_valid():
# #             form.save()
# #     form = ObjectUpdateForm(instance=object)
# #
# #     return render(request, 'app/Object_detail.html', context={'object': object, 'form': form})
# def photo_detail(request, pk):
#     object = get_object_or_404(Object, id=pk, type='photo')
#     return render(request, 'photo_details.html', {'objects': object})
#

#
# def Object_create_view(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         category = request.POST['category']
#         logo = request.FILES['logo']
#         date = request.POST['date']
#         description = request.POST['description']
#         views = request.POST['views']
#         type = request.POST['type']
#
#
#         category_object = category.objects.get(id=category)
#
#         object = Object(
#             title=title,
#             category=category_object,
#             logo=logo,
#             date=date,
#             description=description,
#             views=views,
#             type=type
#         )
#         object.save()
#         return redirect('index')
#
#     return render(request=request, template_name='app/object_create.html')
#
#
# def Object_create_view2(request):
#     if request.method == 'POST':
#         form = ObjectCreateForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     form = ObjectCreateForm()
#
#     return render(request, 'app/object_create2.html', context={'form': form})
#
#
# def Object_delete_view(request, pk):
#     object = Object.objects.get(id=pk)
#     object.delete()
#
#     return redirect('index')
#
from django.shortcuts import render, redirect, get_object_or_404
from .models import Object, Category
from .forms import ObjectCreateForm, ObjectUpdateForm
from django.core.paginator import Paginator
from .forms import SearchForm


def index_view(request):
    objects = Object.objects.all()
    if 'query' in request.GET:
        query = request.GET['query']
        objects = Object.objects.filter(title__icontains=query)

    paginator = Paginator(objects, 3)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(request, 'app/index.html', {'page_obj': page_obj})



def videos_view(request):
    return render(request, 'app/videos.html')


def object_create_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        category_id = request.POST['category']
        logo = request.FILES['logo']
        date = request.POST['date']
        description = request.POST['description']
        views = request.POST['views']
        object_type = request.POST['type']

        category_object = get_object_or_404(Category, id=category_id)

        object = Object(
            title=title,
            category=category_object,
            logo=logo,
            date=date,
            description=description,
            views=views,
            type=object_type
        )
        object.save()
        return redirect('index')

    return render(request, 'app/object_create.html')

def object_create_view2(request):
    if request.method == 'POST':
        form = ObjectCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = ObjectCreateForm()
    return render(request, 'app/object_create2.html', context={'form': form})


# def update_object(request, pk):
#     object_instance = get_object_or_404(Object, pk=pk)
#     if request.method == 'POST':
#         form = ObjectUpdateForm(request.POST, request.FILES, instance=object_instance)
#         if form.is_valid():
#             form.save()
#             return redirect('object_detail', pk=object_instance.pk)
#         form = ObjectUpdateForm(instance=object_instance)
#
#     return render(request, 'objects/update_object.html', {'form': form})


def photo_detail(request, pk):
    object = get_object_or_404(Object, id=pk, type='photo')
    if request.method == 'POST':
        form = ObjectUpdateForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect('photo_detail', pk=object.pk)
    else:
        form = ObjectUpdateForm(instance=object)
    return render(request, 'app/photo_details.html', {'object': object, 'form': form})
def object_delete_view(request, pk):
    obj = get_object_or_404(Object, id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('index')
def about_view(request):
    return render(request, 'app/about.html')

def contact_view(request):
    return render(request, 'app/contact.html')


def object_detail(request, pk):
    obj = get_object_or_404(Object, pk=pk)

    if request.method == 'POST':
        form = ObjectUpdateForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('object_detail', pk=obj.pk)
    else:
        form = ObjectUpdateForm(instance=obj)

    return render(request, 'object_detail.html', {'object': obj, 'form': form})
from .models import Object

def object_list(request):
    objects = Object.objects.all()[:4]
    return render(request, 'your_template.html', {'page_obj': objects})
