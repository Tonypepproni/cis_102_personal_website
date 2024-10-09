from flask import Flask, render_template
from flask.views import View
import csv


cla=Flask(__name__)

class Home(View):
    def __init__(self,temp_name):
        self.temp_name=temp_name

    def dispatch_request(self):
        return render_template(self.temp_name)


templates=[]

with open('template_info.csv', mode ='r')as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            templates.append(line)

for temp in templates:
     cla.add_url_rule(temp['route'],view_func=Home.as_view(temp['name'],temp['template']))

if __name__ == '__main__':
    cla.run(debug=True)