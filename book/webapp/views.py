from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from webapp.forms import BooksForm, BookDeleteForm
from webapp.models import Books


def index_view(request):
    book_list = Books.objects.all().order_by('-created_at')
    return render(request, 'index.html', context={'book_list': book_list})


def book_create_view(request):
    if request.method == "GET":
        form = BooksForm()
        return render(request, 'book_create.html', context={'form': form})
    elif request.method == "POST":
        form = BooksForm(data=request.POST)
        if form.is_valid():
            form = Books.objects.create(
                name=form.cleaned_data.get('name'),
                text=form.cleaned_data.get('text'),
                email=form.cleaned_data.get('email')
            )
            return redirect('index_view')
        return render(request, 'book_create.html', context={'form': form})


def book_update_view(request, id):
    book = get_object_or_404(Books, id=id)

    if request.method == 'GET':
        form = BooksForm(initial={
            'name': book.name,
            'text': book.text,
            'email': book.email
        })
        return render(request, 'book_update.html', context={'form': form, 'book': book})
    elif request.method == 'POST':
        form = BooksForm(data=request.POST)
        if form.is_valid():
            book.name = form.cleaned_data.get("name")
            book.text = form.cleaned_data.get("text")
            book.email = form.cleaned_data.get("email")
            book.save()
            return redirect('index_view')

        return render(request, 'book_create.html', context={'form': form, 'book': book})


def book_delete_view(request, id):
    book = get_object_or_404(Books, id=id)

    if request.method == 'GET':
        form = BookDeleteForm()
        return render(request, 'book_delete.html', context={'book': book, 'form': form})
    elif request.method == 'POST':
        form = BookDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['name'] != book.name:
                form.errors['name'] = ['Имя не совпадает']
                return render(request, 'book_delete.html', context={'book': book, 'form': form})

            book.delete()
            return redirect('index_view')
        return render(request, 'book_delete.html', context={'book': book, 'form': form})