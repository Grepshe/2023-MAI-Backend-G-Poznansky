def application(environ, start_response):
    status = '200 OK'
    body = b'Hello from WSGI'
    headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(body)))
    ]
    start_response(status, headers)
    return [body]
