from virgo.core.routing import routes
from virgo.core.response import Response, redirect
from virgo.core.template import render
from .models import Feedback

def list_create_feedback(request):
    feedback_list = Feedback.all()

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        feedback_type = data.get('feedback_type')
        message = data.get('message')

        Feedback.create(name=name, email=email, feedback_type=feedback_type, message=message)
        return redirect('/feedbacks')
    
    return render('list_create_feedback.html', {'feedback_list':feedback_list}, app='feedback')
routes["/feedbacks"] = list_create_feedback