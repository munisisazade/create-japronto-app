from .app import munis
from .views import index, static_file_handler, methods, api

# static files handler
munis.router.add_route('/static/css/{static_file}', static_file_handler)
munis.router.add_route('/static/js/{static_file}', static_file_handler)
munis.router.add_route('/static/img/{static_file}', static_file_handler)
# Home page
munis.router.add_route('/', index)  # home page

munis.router.add_route('/metod', methods, methods=['GET', 'POST'])
munis.router.add_route('/api', api)
