from flask import Flask, render_template
from flask.views import View
import csv


cla=Flask(__name__)

class Basic(View):
    def __init__(self,temp_name,title,page_title,sites):
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
        self.sites=sites

    def csv_reader(self,file_name,list):
        with open(f'static/info/{file_name}',mode='r') as file:
            csvFile=csv.DictReader(file)
            for line in csvFile:
                list.append(line)
        return list

    def dispatch_request(self):
        return render_template(
            self.temp_name,
            title=self.title,
            page_title=self.page_title,
            nav_items=self.nav_items,
            sites=self.sites
        )

class Collect(Basic):
                 
    def dispatch_request(self):
        
        self.cards=[]
        self.maps=[]
            
        self.cards=Basic.csv_reader(self,'mtg_cards.csv',self.cards)
        self.maps=Basic.csv_reader(self,'maps.csv',self.maps)

        return render_template(
        self.temp_name,
        title=self.title,
        page_title=self.page_title,
        nav_items=self.nav_items,
        sites=self.sites,
        cards=self.cards,
        maps=self.maps
        )

class Media(Basic):

        def dispatch_request(self):            

            self.movies=[]
            self.tv_shows=[]

            return render_template(
            self.temp_name,
            title=self.title,
            page_title=self.page_title,
            nav_items=self.nav_items,
            sites=self.sites,
            all_movies=self.movies,
            all_shows=self.tv_shows
            )

templates=[]

with open('template_info.csv', mode ='r')as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            templates.append(line)

sites=[]

for i in templates:
     sites.append({'name':i['name'],'url':i['route']})

for temp in templates:
    if temp['type']=='collect':
        cla.add_url_rule(temp['route'],view_func=Collect.as_view(temp['name'],temp['template'],temp['name'],temp['page_title'],sites))
    elif temp['type']=='media':
        cla.add_url_rule(temp['route'],view_func=Media.as_view(temp['name'],temp['template'],temp['name'],temp['page_title'],sites))         
    else:
        cla.add_url_rule(temp['route'],view_func=Basic.as_view(temp['name'],temp['template'],temp['name'],temp['page_title'],sites))

if __name__ == '__main__':
    cla.run(debug=True)