from flask import Flask, render_template
from flask.views import View
import csv


cla=Flask(__name__)

class Home(View):
    def __init__(self,temp_name,title,page_title,templates):
        self.temp_name=temp_name
        self.title=title
        self.page_title=page_title
        self.nav_items=[
            {'name':'home','url':'/'},
            {'name':'socials','url':'/socials'},
            {'name':'travel','url':'/travel'},
            {'name':'collection','url':'/collect'},
            {'name':'media','url':'/media'}
        ]

    def dispatch_request(self):
        return render_template(self.temp_name,title=self.title,page_title=self.page_title,nav_items=self.nav_items)

templates=[]

with open('template_info.csv', mode ='r')as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            templates.append(line)

for temp in templates:
     cla.add_url_rule(temp['route'],view_func=Home.as_view(temp['name'],temp['template'],temp['name'],temp['page_title']))

if __name__ == '__main__':
    cla.run(debug=True)