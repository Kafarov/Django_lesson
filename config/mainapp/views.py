from django.shortcuts import render


def index(reqest):
    return render(reqest, 'mainapp/index.html')


def contacts(reqest):
    return render(reqest, 'mainapp/contacts.html')


def courses(reqest):
    return render(reqest, 'mainapp/courses_list.html')


def doc_site(reqest):
    return render(reqest, 'mainapp/doc_site.html')


def login(reqest):
    return render(reqest, 'mainapp/login.html')


def news(reqest):
    cnt = range(5)
    return render(reqest, 'mainapp/news.html', {'range': cnt})

def news_with_pagiinator(reqest, pk):
    cnt = range(5)
    return render(reqest, 'mainapp/news.html', {'range': cnt})