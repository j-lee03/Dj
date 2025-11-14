from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
# Create your views here.
def bookmark_list(request):
    bookmarks =Bookmark.objects.filter(id__gte=50)

    context = {
        'bookmarks':bookmarks
    }
    return render(request, template_name='bookmark/bookmark_list.html', context=context)



def bookmark_detail(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except:
        raise Http404

    context={'bookmark':bookmark}
    return render(request, template_name='bookmark/bookmark_detail.html', context=context)