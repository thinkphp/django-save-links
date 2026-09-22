from django.shortcuts import render, redirect
from .forms import LinkForm
from .models import Link


def home(request):
    links = Link.objects.all()

    if request.method == "POST":
        form = LinkForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = LinkForm()

    return render(request, "links/home.html", {
        "form": form,
        "links": links,
    })
