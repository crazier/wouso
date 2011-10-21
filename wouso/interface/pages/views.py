from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from wouso.interface import logger
from models import StaticPage, NewsItem

def staticpage(request, slug):
    """ Perform regular search by either first or last name """
    staticpage = StaticPage.objects.get(slug=slug)
    return render_to_response('static_page.html',
                              {'staticpage': staticpage},
                              context_instance=RequestContext(request))

def news_index(request, page=u'1'):
    all_news = NewsItem.objects.all().order_by('-date_pub')

    paginator = Paginator(all_news, 10)
    try:
        news_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news_page = paginator.page(paginator.num_pages)

    return render_to_response('news_index.html',
                            {'news_page': news_page},
                              context_instance=RequestContext(request))

def news_item(request, item_id):
    n = get_object_or_404(NewsItem, pk=item_id)

    return render_to_response('news_item.html',
                            {'n': n},
                              context_instance=RequestContext(request))
