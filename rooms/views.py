# from math import ceil
# from django.shortcuts import render
# from django.core.paginator import Paginator
from django.views.generic import ListView
# from django.http import HttpResponse
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"    
    context_object_name = "rooms"

# def all_rooms(request):
    # page = int(request.GET.get("page", 1))
    # page = int(page or 1)
    # page_size = 10
    # limit = page * page_size
    # offset = limit - page_size
    # all_rooms = models.Room.objects.all()[offset:limit]
    # page_count = ceil(models.Room.objects.count() / page_size)
    # return render(
    #     request,
    #     "rooms/home.html",
    #     {
    #         "potato": all_rooms,
    #         "page": page,
    #         "page_count": page_count,
    #         "page_range": range(1, page_count),
    #     },
    # )
    # page = request.GET.get("page", 1)
    # room_list = models.Room.objects.all()
    # paginator = Paginator(room_list, 10, orphans=5)
    # rooms = paginator.page(int(page))
    # return render(request, "rooms/home.html", {"page": rooms})