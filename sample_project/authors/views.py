from django.shortcuts import render, get_object_or_404
from .forms import AuthorForm
from .models import Author


# Create your views here.

def author_detail_view(request, id):
    author = get_object_or_404(Author, id=id)
    form = AuthorForm(instance=author)
    return render(request, 'author_detail.html', {'form': form})
