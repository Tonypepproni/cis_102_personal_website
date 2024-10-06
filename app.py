from flask import Flask, render_template, url_for
import csv

app = Flask(__name__)

@app.context_processor
def nav_items_inject():
    nav_items=[
        {'name':'home','url':'/'},
        {'name':'socials','url':'/socials'},
        {'name':'travel','url':'/travel'},
        {'name':'collection','url':'/collect'},
        {'name':'media','url':'/media'}
    ]
    sites=[
        {'name':'home','url':'/'},
        {'name':'socials','url':'/socials'},
        {'name':'travel','url':'/travel'},
        {'name':'collection','url':'/collect'},
        {'name':'media','url':'/media'},
        {'name':'site map','url':'/site_map'}
    ]

    return dict(nav_items=nav_items,sites=sites)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/socials')
def socials():
    return render_template('socials.html')

@app.route('/travel')
def travel():
    return render_template('travel.html')

@app.route('/media')
def media():
    tv_shows=[]
    movies=[]

    file = open("static/info/tv_show.txt",'r')

    for i in file:
        tv_shows.append(i)

    file.close()

    file = open("static/info/movies.txt","r")

    for i in file:
        movies.append(i)

    file.close()

    return render_template('media.html',all_movies=movies,all_shows=tv_shows)

@app.route('/collect')
def collect():
    
    cards = []
    maps = []
    pins = []
    coins = []

    with open('static/info/mtg_cards.csv', mode ='r')as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            cards.append(line)

    with open('static/info/maps.csv', mode='r') as file:
        csvFile = csv.DictReader(file)
        for line in csvFile:
            maps.append(line)

    return render_template('collect.html',cards=cards,maps=maps)

@app.route('/site_map')
def site_map():
    return render_template("site_map.html")

if __name__ == "__main__":
    app.run(debug=True)