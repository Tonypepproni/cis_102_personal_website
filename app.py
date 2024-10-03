from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.context_processor
def nav_items_inject():
    nav_items=[
        {'name':'home','url':'/'},
        {'name':'socials','url':'/socials'},
        {'name':'travel','url':'/travel'},
        {'name':'collections','url':'/collect'}
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

app.route('/collect')
def collect():
    cards=[
        {'name':'jeweled lotus','set':'commander'}
    ]

    return render_template('collect.html',cards=cards)

if __name__ == "__main__":
    app.run(debug=True)