import os
from jinja2 import Template
from conf import settings
from http.cookies import SimpleCookie
from firebase_admin import db, storage

TEMP_DIR = settings.TEMP_DIR
BASE_DIR = settings.BASE_DIR


def index(request):
    template = open(TEMP_DIR + 'index.html')
    django_template = Template(template.read())
    name = request.match_dict
    print(name)
    reqem = ['alma', 'armut']
    return request.Response(text=django_template.render(name=name, data=reqem), mime_type='text/html')


async def static_file_handler(request):
    path = request.match_dict['static_file'].strip('/')
    try:
        if '.css' in path:
            with open(BASE_DIR + '/static/css/' + path) as css_file:
                return request.Response(text=css_file.read(), mime_type='text/css')
        elif '.js' in path:
            with open(BASE_DIR + '/static/js/' + path) as js_file:
                return request.Response(text=js_file.read(), mime_type='text/javascript')
        elif '.png' in path:
            with open(BASE_DIR + '/static/img/' + path, 'rb') as png_file:
                return request.Response(body=png_file.read(), mime_type='image/png')
        elif '.jpg' in path:
            with open(BASE_DIR + '/static/img/' + path, 'rb') as html_file:
                return request.Response(body=html_file.read(), mime_type='image/jpg')
    except:
        return request.Response(text="File not found")


def methods(request):
    if request.method == 'POST':
        text = "You send a post request"
    else:
        text = "You send a Get request"
    return request.Response(text=text)


def api(request):
    return request.Response(json={"cool": "Be cool", "awesome": "tool", "japronto": "<3"})


def firebase_test(request):
    template = open(TEMP_DIR + 'article.html')
    django_template = Template(template.read())
    bucket = storage.bucket('munis')
    bucket
    messages = db.reference('testing/')
    data = messages.get()
    return request.Response(text=django_template.render(data=data), mime_type='text/html')


def contact_us(request):
    template = open(TEMP_DIR + 'article.html')
    django_template = Template(template.read())
    users = db.reference('users/')
    if request.method == 'GET':
        data = {}
        return request.Response(text=django_template.render(data=data), mime_type='text/html')
    else:
        # request_data = []
        #
        # request_data.append({"request.files": request.files})
        # request_data.append({"request.form": request.form})
        data = {}
        if request.form:
            for key, value in request.form.items():
                data[key] = value
        users.set(data)
        return request.Response(text=django_template.render(data=data), mime_type='text/html')


def request_info(request):
    text = """Basic request properties:
      Method: {0.method}
      Path: {0.path}
      HTTP version: {0.version}
      Query string: {0.query_string}
      Query: {0.query}!""".format(request)

    if request.cookies:
        text += "\nCookies all:\n"
        for name, value in request.headers.items():
            text += "{0}: {1}\n".format(name, value)
    # request.cookies = request.cookies.pop('city')
    # request.cookies = request.cookies.pop('hello')
    text += str(dir(request.cookies))
    # request.cookies = request.cookies.pop('hello', None)
    data = request.Response(text=text)
    new_data = str(dir(request.cookies))
    return data
