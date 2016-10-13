from django.shortcuts import render
from models import LibraryPath
from forms import LibraryPathForm


# Create your views here.
def index(request, **kwargs):

    paths = LibraryPath.objects.all()

    context = {'paths': paths}

    return render(request, 'configs/index.html', context)


def navigator(request, **kwargs):
    """Computer disk navigator and path saving functionality"""
    import os
    import psutil
    from django.contrib import messages

    destination = ''
    dirs = []
    files = []

    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = LibraryPathForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully added the path. It would be used for importing media into Collection.')
        else:
            messages.add_message(request, messages.INFO, 'Could not add the path. Already exists.')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LibraryPathForm()

    drives = [each.mountpoint for each in psutil.disk_partitions() if 'fixed' in each.opts]

    if request.GET.get('dir'):
        destination = request.GET.get('dir')
        try:
            os.chdir(destination)
        except Exception as e:
            messages.add_message(request, messages.WARNING, "Access Denied")

        dirs = [each for each in os.listdir(os.getcwd()) if os.path.isdir(each)]
        files = [each for each in os.listdir(os.getcwd()) if os.path.isfile(each)]
        current = os.getcwd()
    else:
        current = 'Computer Root'

    context = {'parent': destination, 'current': current, 'drives': drives, 'dirs': dirs, 'files': files, 'form': form}

    return render(request, 'configs/navigator.html', context)