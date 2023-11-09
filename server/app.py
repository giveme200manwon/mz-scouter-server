import cherrypy
from calculate_power import calculate_power


@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    @cherrypy.tools.json_out()
    def GET(self):
        return {'msg': 'hello'}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        power = calculate_power(data)
        return {'id': data['test_id'], 'power': power}


if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0',
              'server.socket_port': 8888}
    cherrypy.config.update(config)
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
