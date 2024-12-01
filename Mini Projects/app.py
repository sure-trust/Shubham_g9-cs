from flask import Flask, render_template, request

app = Flask(__name__)

# Simple Caesar Cipher for encoding and decoding

def encode_text(text):
    return ''.join([chr(ord(char) + 3) for char in text])

def decode_text(text):
    return ''.join([chr(ord(char) - 3) for char in text])

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        action = request.form['action']
        if action == 'encode':
            result = encode_text(text)
        elif action == 'decode':
            result = decode_text(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)