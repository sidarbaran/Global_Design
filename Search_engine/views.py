from django.shortcuts import render

# Create your views here.
def contact_us(request):
    if request.method=='GET':
        return render(request, 'contact.html', {
    })
def base(request):
    if request.method=='GET':
        return render(request, 'base.html', {
    })
def about(request):
    if request.method=='GET':
        return render(request, 'about_us.html', {
    })
def search_result(request):
    if request.method=='GET':
        return render(request, 'Search_result.html', {
    })
def recom(request):
    if request.method=='GET':
        return render(request, 'recommendation.html', {
    })
def books(request):
    if request.method=='GET':
        return render(request, 'Search_book.html', {
    })
