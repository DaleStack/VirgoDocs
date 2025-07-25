from virgo.core.routing import routes
from virgo.core.response import Response, redirect
from virgo.core.template import render


def docs_page(request, page):
    page_name = request.path.split("/")[-1] or "overview"
    context = {
        "current_path": request.path,
        "page": page_name
    }
    return render("documentation.html", {"context":context}, app="docs")
routes["/docs/<page>"] = docs_page


