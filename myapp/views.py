from django.shortcuts import render, HttpResponse
import random

# Create your views here.
topics = [
    {'id':1, 'title':'routing 알아보기', 'body':'Routing is ..'},
    {'id':2, 'title':'view 알아보기', 'body':'View is ..'},
    {'id':3, 'title':'Model 알아보기', 'body':'Model is ..'}
]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'  # <li>routing</li> 등을 대체

    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ol>
            {ol}
        </ol>
        {articleTag}
    </body>
    </html>     
    '''

# 클라이언트로 정보를 전달하는 함수
def index(request):
    article = """
    <h2>Welcome</h2>
    Hello, Django
    """
    return HttpResponse(HTMLTemplate(article)) # reponse through http

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article))

def create(request):
    return HttpResponse("Create")







# def read(request, id):
#     return HttpResponse("Read!" + id)


# DYNAMIC web application server
# def index(request):
#     return HttpResponse("<h1>Random</h1>" + str(random.random())) # reponse through http

# <a> 는 링크시키기 위해 사용하는 태크
# href 속성은 hypertext reference로 연결할 주소 지정하는 속성

