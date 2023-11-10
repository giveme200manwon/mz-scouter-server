import cherrypy
from dotenv import load_dotenv
import os
from work_queue import WorkQueue

@cherrypy.expose
class AnalysisAPIServer(object):
    work_queue = WorkQueue()
    @cherrypy.tools.json_out()
    def GET(self):
        return AnalysisAPIServer.work_queue.popQueue()
    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        ClientAPIServer.results.append(data)
        return {}


@cherrypy.expose
class ClientAPIServer(object):
    results = []

    @cherrypy.tools.json_out()
    def GET(self, test_id):
        for idx, result in enumerate(ClientAPIServer.results):
            if result['test_id'] == test_id:
                return ClientAPIServer.results.pop(idx)
        return {'msg': 'No such test id'}

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        data = cherrypy.request.json
        AnalysisAPIServer.work_queue.addQueue(data)
        return {}


if __name__ == '__main__':
    load_dotenv()

    config = {'server.socket_host': '0.0.0.0',
              'server.socket_port': int(os.getenv('PORT'))}
    cherrypy.config.update(config)
    client_conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    analysis_conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.tree.mount(ClientAPIServer(), '/', client_conf)
    cherrypy.tree.mount(AnalysisAPIServer(), '/analysis', analysis_conf)
    
    cherrypy.engine.start()
    cherrypy.engine.block()
