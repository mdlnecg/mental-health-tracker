from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306207846',
        'name': 'Madeline Clairine Gultom',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)