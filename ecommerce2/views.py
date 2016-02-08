from django.shortcuts import render

def blank(request):
	return render(request, "blank.html", {})

def about(request):
	return render(request, "about.html", {})

def faq(request):
	return render(request, "faq.html", {})

def services(request):
	return render(request, "service.html", {})

def term(request):
	return render(request, "term.html", {})

def gallery(request):
	return render(request, "gallery.html", {})

def tour(request):
	return render(request, "tour.html", {})

def custom_404(request):
	return render(request, "404.html", {})

def custom_500(request):
	return render(request, "500.html", {})


