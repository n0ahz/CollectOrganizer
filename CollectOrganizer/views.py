# from django.http import HttpResponse
from django.shortcuts import render


def home(request, **kwargs):
    """The Landing page"""
    return render(request, 'CollectOrganizer/index.html')


def about(request, **kwargs):
    """About the product"""
    return render(request, 'CollectOrganizer/about.html')


def not_available(request, **kwargs):
    """Future implementations"""
    return render(request, 'CollectOrganizer/unavailable.html')


def admin(request, **kwargs):
    """Easy access to django admin"""
    return render(request, 'CollectOrganizer/admin.html')