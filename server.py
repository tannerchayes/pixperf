from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        print('doint get')

        if self.path == '/':
            self.path = '/index.html'


        try:
            print(self.path[1:])
            with open(self.path[1:], 'r') as test_file:
                template = test_file.read()
            self.send_response(200)

        except:
            template = "File not found"
            self.send_response(404)


        context = {
            'blog_posts': """
                <div class="group relative h-[300px] w-[270px]">
                    <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                    <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                    <div class="relative">
                    <h2 class="text-gray-600 text-lg align-text-bottom">Another Cool Post</h2>
                    </div>
                </div>
        
                <div class="group relative h-[300px] w-[270px]">
                    <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                    <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                    <div class="relative">
                    <h2 class="text-gray-600 text-lg">Post Title</h2>
                    </div>
                </div>
        
                <div class="group relative h-[300px] w-[270px]">
                    <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                    <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                    <div class="relative">
                    <h2 class="text-gray-600 text-lg">Another Longer Post Title</h2>
                    </div>
                </div>
        
                <div class="group relative h-[300px] w-[270px]">
                    <img class="absolute inset-0 object-cover w-full h-full" src="img/Surf-Ad.jpeg">
                    <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                    <div class="relative">
                    <h2 class="text-gray-600 text-lg">Oh Cool, A Post!</h2>
                    </div>
                </div>
            """
        }

        processed_template = template
        for ctx_variables in context.keys():
            processed_template = processed_template.replace('{{ ' + ctx_variables + ' }}', context.get(ctx_variables))

        self.end_headers()
        self.wfile.write(bytes(processed_template, 'utf-8'))


httpd = HTTPServer(('localhost', 8000), Serv)
httpd.serve_forever()
