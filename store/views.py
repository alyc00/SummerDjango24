from django.shortcuts import render, get_object_or_404
from .models import Show, Studio
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse


# Create your views here.


class ShowListView(ListView):
    model = Show
    template_name = "shows_list.html"
    context_object_name = "all_shows_list"


class ShowDetailView(DetailView):
    model = Show
    template_name = "shows_detail.html"


class ShowCreateView(CreateView):
    model = Show
    template_name = 'shows_new.html'
    fields = ["title", "show_id", "studio", "description", "num_of_episodes", "num_of_seasons", "image", "type", "price", "featured"]
    

class ShowDeleteView(DeleteView):
    model = Show
    template_name = 'shows_delete.html'


class ShowUpdateView(UpdateView):
    model = Show
    template_name = 'shows_edit.html'


def home_page(request):
    return render(request, 'store/home.html', {})


def shows_list(request):
    shows = Show.objects.all()

    return render(request, 'store/shows_list.html', {'shows': shows})


def shows_detail(request, id, title, c):
    show = get_object_or_404(Show, id=id, title=title, )

    return render(request, 'store/shows_detail.html', {'show': show})


def search_page(request):
    return render(request, 'store/search.html', {})


def about_page(request):
    return render(request, 'store/about.html', {})