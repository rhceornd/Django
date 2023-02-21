from django.shortcuts import render, HttpResponse
import random

# Create your views here.
topics = [
    {'id':1, 'title':'routing 알아보기', 'body':'Routing is ..'},
    {'id':2, 'title':'view 알아보기', 'body':'View is ..'},
    {'id':3, 'title':'Model 알아보기', 'body':'Model is ..'}
]
# 클라이언트로 정보를 전달하는 함수
def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'  # <li>routing</li> 등을 대체
    return HttpResponse(f"""
    <html>
    <body>
        <h1>Django</h1>
        <ol>
            {ol}
        </ol>
        <h2>Welcome</h2>
        Hello, Django
    </body>
    </html>    
    """) # reponse through http

def read(request, id):
    return HttpResponse("Read!" + id)

def create(request):
    return HttpResponse("Create")







# def read(request, id):
#     return HttpResponse("Read!" + id)


# DYNAMIC web application server
# def index(request):
#     return HttpResponse("<h1>Random</h1>" + str(random.random())) # reponse through http

# <a> 는 링크시키기 위해 사용하는 태크
# href 속성은 hypertext reference로 연결할 주소 지정하는 속성

