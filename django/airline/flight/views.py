from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.
def index(request):
    context = {
        "flights" : Flight.objects.all()
    }
    return render(request, "flight/index.html", context)

def flight(request, flightid):
    try:
        flight = Flight.objects.get(pk=flightid)
    except Flight.DoesNotExist:
        raise Http404("Flight Doesnot exist")

    context = {
        "flight" : flight,
        "passengers" : flight.passenger.all(),
        "non_passenger" : Passenger.objects.exclude(flights=flightid)
    }
    return render(request, "flight/flight.html", context)


def book(request, flightid):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flightid)
    except KeyError:
        raise Http404("No selection")
    except Passenger.DoesNotExist:
        raise Http404("No passenger")
    except Flight.DoesNotExist:
        raise Http404("No flight")

    passenger.flights.add(flight)

    return HttpResponseRedirect(reverse("flight", args=(flightid,)))




























        #
