from django.shortcuts import render


def index(request):
    context = {
        'turn_on_block': True,
    }
    return render(request, 'main/index.html', context)
