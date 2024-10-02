from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():

    with open('names.txt', 'r') as file:
        file_content=file.read()

    file_content = file_content.replace('\n','<br><br>')

    return render_template('index.html',content=file_content)

if __name__ == "__main__":
    app.run(debug=True)