from virgo.core.routing import routes
from virgo.core.response import Response, redirect
from virgo.core.template import render

def about_page(request):
    return render("about.html", app="about")
routes["/about"] = about_page
