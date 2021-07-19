import tornado.ioloop
import tornado.web
import datetime

serverStartTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
serverName = "Tornado server"

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("request")
        requestTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = {"Server Start Time": serverStartTime,
                    "Request Time": requestTime,
                    "Server Name": serverName}
        self.write(response)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()