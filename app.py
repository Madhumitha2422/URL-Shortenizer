from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_database = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form.get('long_url')
    custom_alias = request.form.get('custom_alias')

    if custom_alias:
        alias = custom_alias
    else:
        alias = generate_alias()

    short_url = request.url_root + alias
    url_database[alias] = long_url

    return render_template('result.html', long_url=long_url, short_url=short_url)

@app.route('/<alias>')
def redirect_to_long_url(alias):
    if alias in url_database:
        long_url = url_database[alias]
        return redirect(long_url)
    else:
        return "Alias not found", 404

def generate_alias():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

if __name__ == '__main__':
    app.run(debug=True)
