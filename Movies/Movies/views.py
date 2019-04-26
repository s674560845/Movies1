from django.http import HttpResponse


def index(request):
    return HttpResponse("欢迎来到我的爬虫网页！")