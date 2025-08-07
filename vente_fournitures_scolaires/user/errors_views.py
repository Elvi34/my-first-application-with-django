
from django.shortcuts import render



def error_404_view(request, exception):

    """

    View to handle 404 errors.

    """

    return render(request, 'errors/404.html', status=404)



def error_403_view(request, exception):

    """

    View to handle 403 errors.

    """

    return render(request, 'errors/403.html', status=403)



def error_500_view(request):

    """

    View to handle 500 errors.

    """

    return render(request, 'errors/500.html', status=500)



def error_400_view(request, exception):

    """

    View to handle 400 errors.

    """

    return render(request, 'home/pages/errors/500.html', status=400) 