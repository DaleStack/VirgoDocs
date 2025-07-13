from virgo.core.routing import routes
from virgo.core.response import Response, redirect
from virgo.core.template import render


def landing_page(request):
    return render("landing_page.html", app="landing")
routes["/"] = landing_page
