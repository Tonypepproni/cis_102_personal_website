from flask import Flask, render_template, url_for

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
    return dict(nav_items=nav_items)

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

    file = open("tv_show.txt",'r')

    for i in file:
        tv_shows.append(i)

    file.close()

    left_shows=tv_shows[len(tv_shows)//2:]
    right_shows=tv_shows[:len(tv_shows)//2]

    file = open("movies.txt","r")

    for i in file:
        movies.append(i)

    file.close()

    left_movies=movies[len(movies)//2:]
    right_movies=movies[:len(movies)//2]

    return render_template('media.html',left_movies=left_movies,right_movies=right_movies,left_shows=left_shows,right_shows=right_shows)

@app.route('/collect')
def collect():
    cards=[
        {'name':'jeweled lotus','set':'commander'}
    ]

    return render_template('collect.html',cards=cards)

@app.route('/sitemap')
def sitemap():

    sites=[
        {'name':'home','url':'/'},
        {'name':'socials','url':'/socials'},
        {'name':'travel','url':'/travel'},
        {'name':'collection','url':'/collect'},
        {'name':'media','url':'/media'},
        {'name':'site map','url':'/sitemap'}
    ]

    return render_template("site_map.html",sites=sites)

if __name__ == "__main__":
    app.run(debug=True)