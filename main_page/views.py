from django.shortcuts import render, redirect
from .models import Category, Dish, Chef, Why_us, Response, Event, Gallery, About, Footer
from .forms import UserReservationForm, UserContactForm
from django.http import HttpRequest, HttpResponse


def main_view(request: HttpRequest) -> HttpResponse:
    """
    The function that will render the response to the user.
    :param request: request.
    :return: response.
    """
    form_reserve = UserReservationForm(request.POST or None)
    form_contact = UserContactForm(request.POST or None)

    if form_reserve.is_valid():
        form_reserve.save()
        return redirect('/')

    if form_contact.is_valid():
        form_contact.save()
        return redirect('/')

    dishes = Dish.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    chefs = Chef.objects.filter(is_visible=True)
    why_us = Why_us.objects.filter(is_visible=True)
    response = Response.objects.filter(is_visible=True)
    events = Event.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    about = About.objects.filter(is_visible=True)
    footer = Footer.objects.all()

    return render(request, 'base.html', context={
        'categories': categories,
        'dishes': dishes,
        'chefs': chefs,
        'why_us': why_us,
        'response': response,
        'events': events,
        'gallery': gallery,
        'form_reserve': form_reserve,
        'about': about,
        'form_contact': form_contact,
        'footer': footer
    })
