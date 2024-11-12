
from http.server import HTTPServer, SimpleHTTPRequestHandler


class BlogServer(SimpleHTTPRequestHandler):

    # def get_context_data(self):
    #     ctx = {}
    #
    #     ctx['blog_posts'] = """<ul><li>Blog 1</li><li>Blog 2</li><li>Blog 3</li></ul>"""
    #     ctx['heading'] = """<h1>Heading</h1>"""
    #
    #     print(ctx['blog_posts'])
    #
    #     return ctx
    #
    # def render_template(self, template, context):
    #     template = str(template, 'utf-8')
    #     for template_var in context.keys():
    #         template = template.replace('{{ ' + template_var + ' }}', context[template_var])
    #
    #     return bytes(template, 'utf-8')

    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            try:
                if self.path.endswith('.html') or self.path.endswith('/'):
                    template = f.read()

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
                        processed_template = processed_template.replace('{{ ' + ctx_variables + ' }}',
                                                                        context.get(ctx_variables))

                    # template = self.render_template(template, self.get_context_data())
                    self.end_headers()
                    self.wfile.write(processed_template)
                else:
                    self.copyfile(f, self.wfile)
            finally:
                f.close()

    def send_header(self, keyword, value):
        """Don't send content-length heading since it's wrong in send_head()"""
        if keyword == 'Content-Length':
            pass
        else:
            super().send_header(keyword, value)


httpd = HTTPServer(('localhost', 8000), BlogServer)
httpd.serve_forever()
