from django.shortcuts import render


# def projects(request):
#     return render(request, 'base.html')


def Home_Page(request):
    pk = 'Hello'
    context = {
        'pk': pk,
    }
    return render(request, 'HOME/home-page.html', context)
