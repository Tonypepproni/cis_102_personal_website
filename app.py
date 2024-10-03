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
    with open('tv_show.txt','r') as file:
        x=file.read()
        x.replace('\n','<br><br>')
        tv_shows.append(x)
        print(tv_shows)

    with open('movies.txt','r') as file:
        file_content=file.read()

    file_content.replace('\n','<br><br>')
    print(file_content)

    return render_template('media.html',content=file_content,tvcontent=tv_shows)

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