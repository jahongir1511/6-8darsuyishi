from django.views.generic import ListView, DetailView, CreateView, DeleteView, View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import AddReviewForm
from .models import Books, Review

class BookListView(View):
    def get(self, request):
        books = Books.objects.all().order_by('-id')
        return render(request, 'book/book_list.html', {'books': books})

class BookDetailView(View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        reviews = Review.objects.filter(book=pk)
        context = {'book': book, 'reviews': reviews}
        return render(request, 'book/book_detail.html', context=context)

class BookCreateView(CreateView):
    model = Books
    template_name = 'book/book_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:book-list')

class BookDeleteView(DeleteView):
    model = Books
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('products:book-list')

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        book = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {'book': book, 'add_review_form': add_review_form}
        return render(request, 'book/add_review.html', context=context)

    def post(self, request, pk):
        book = Books.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                book=book,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )
            review.save()
            return redirect('products:book-detail', pk=pk)
        return render(request, 'book/add_review.html', {'book': book, 'add_review_form': add_review_form})