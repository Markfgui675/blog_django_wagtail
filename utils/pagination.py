import math
from django.core.paginator import Paginator

def make_pagination_range(
    page_range,
    qtd_padingas,
    current_page
):
    middle_range = math.ceil(qtd_padingas / 2)
    start_range = current_page -  middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range+=abs(start_range_offset)
    
    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination = page_range[start_range:stop_range]
    return {
        'pagination':pagination,
        'page_range':page_range,
        'qty_pages':qtd_padingas,
        'current_page':current_page,
        'total_page':total_pages,
        'start_range':start_range,
        'stop_range':stop_range,
        'first_page_out_of_range':current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages
    }


def make_pagination(request, object_list, per_page=5, qtd_pages=4):

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

        
    paginator = Paginator(object_list=object_list, per_page=per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(page_range=paginator.page_range, qtd_padingas=qtd_pages, current_page=current_page)

    return {
        'page_obj':page_obj,
        'pagination_range':pagination_range
    }
