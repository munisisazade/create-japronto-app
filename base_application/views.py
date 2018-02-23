import os
from jinja2 import Template
from conf import settings

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
    return request.Response(json={"cool":"Be cool", "awesome":"tool","japronto":"<3"})
