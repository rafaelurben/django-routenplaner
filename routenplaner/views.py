from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required, permission_required

from .models import Route

# Create your views here.


@login_required
@permission_required("routenplaner.view_route")
def view_route(request, object_id):
    if Route.objects.filter(id=int(object_id)).exists():
        obj = Route.objects.get(id=int(object_id))
        return render(request, "routenplaner/view-route.html", {
            "route": obj,
            "orte": obj.get_orte(),
        })
    else:
        messages.error(request, "Route konnte nicht gefunden werden!")
        return redirect(reverse("admin:routenplaner_route_changelist"))


@login_required
@permission_required("routenplaner.view_route")
def routes(request):
    return render(request, "routenplaner/routes.html", {
        "routes": Route.objects.all(),
    })


def manifest(request):
    response = render(request, "routenplaner/manifest.json", {})
    response['Content-Type'] = 'text/json'
    response["Service-Worker-Allowed"] = "/"
    return response
