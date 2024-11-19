import csv
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

    def render_template(self, template, context):
        for template_var in context.keys():
            template = template.replace('{{ ' + template_var + ' }}', context[template_var])

        return template

    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            try:
                if self.path.endswith('.html') or self.path.endswith('/'):
                    #    read the html file
                    with open('index.html', 'r', encoding='utf-8') as template_file:
                        template = template_file.read()

                    template_yes = """
                        <div class="group relative h-[300px] w-[270px]">
                            <img class="absolute inset-0 object-cover w-full h-full" src="img/{{ image }}">
                            <div class="absolute top-[0px] bottom-[0px] left-[0px] right-[0px] bg-sky-800 opacity-60 group-hover:hidden"></div>
                            <div class="relative">
                            <h2 class="text-gray-600 text-lg align-text-bottom">{{ title }}</h2>
                            </div>
                        </div>
                    """
                    with open('csv(2)', 'r', encoding='utf-8') as csv_file:
                        csv_reader = csv.DictReader(csv_file)

                        blog_post_html = ""
                        for row in csv_reader:
                            context = {
                                'image': row['image'],
                                'title': row['title'],
                            }

                            post_html = self.render_template(template_yes, context)
                            blog_post_html += post_html


                    context = {
                        'blog_posts': blog_post_html,
                    }

                    processed_template = self.render_template(template, context)
                    # processed_template = str(template, 'utf-8')
                    # for ctx_variables in context.keys():
                    #     processed_template = processed_template.replace('{{ ' + ctx_variables + ' }}',
                    #                                                     context.get(ctx_variables))

                    # template = self.render_template(template, self.get_context_data())
                    self.end_headers()
                    self.wfile.write(bytes(processed_template, 'utf-8'))
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


if __name__ == '__main__':
    print("hello")

httpd = HTTPServer(('localhost', 8000), BlogServer)
httpd.serve_forever()

