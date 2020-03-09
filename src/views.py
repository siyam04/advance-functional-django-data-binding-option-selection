from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q


class HomeView(TemplateView):
    template_name = 'home.html'
