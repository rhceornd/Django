from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random

nextId = 4

topics = [
    {'id':1, 'title':'routing 알아보기', 'body':'Routing is ..'},
    {'id':2, 'title':'view 알아보기', 'body':'View is ..'},
    {'id':3, 'title':'Model 알아보기', 'body':'Model is .. 블라블라'}
]

# HTML 형식
def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    # post 방식으로 delete 실행.
    # id가 있다면 delete 버튼을 생성
    # post 방식으로 id를 송신
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id", value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li>
                <a href="/update/{id}">update</a>
            </li>
        '''
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
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>

    </body>
    </html>     
    '''

# 클라이언트로 정보를 전달하는 함수
def index(request):
    article = """
    <h2>Welcome</h2>
    Hello, Django
    This is DY homepage
    """
    return HttpResponse(HTMLTemplate(article)) # reponse through http

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

# title, body를 서버에 원하는 패스로 보내기 위해서 form tag로 감싸야함.
# form 에 method를 따로 지정하지 않으면 get 방식으로 요청
@csrf_exempt
def create(request):
    global nextId
    # print("request method :", request.method)
    if request.method == 'GET':
        article = """
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        """
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/'+ str(nextId)
        nextId += 1

        return redirect(url)

@csrf_exempt
def update(request, id):
    global topics
    if request.method == "GET":
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                }
        article = f"""
                    <form action="/update/{id}" method="post">
                        <p><input type="text" name="title" placeholder="title", value={selectedTopic["title"]}></p>
                        <p><textarea name="body" placeholder="body">{selectedTopic["body"]}</textarea></p>
                        <p><input type="submit"></p>
                    </form>
                """
        return HttpResponse(HTMLTemplate(article, id))

    elif request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')

@csrf_exempt
def delete(request):
    global  topics
    if request.method == 'POST':
        id = request.POST['id']
        # print('id :', id)

        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')





# def read(request, id):
#     return HttpResponse("Read!" + id)


# DYNAMIC web application server
# def index(request):
#     return HttpResponse("<h1>Random</h1>" + str(random.random())) # reponse through http

# <a> 는 링크시키기 위해 사용하는 태크
# href 속성은 hypertext reference로 연결할 주소 지정하는 속성

