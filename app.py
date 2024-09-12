from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')  # Home page
def serve_html():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>cat-website</title>  
        <style>
            body {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                text-align: center;
            }
            h1 {
                margin-bottom: 20px;
            }
            img {
                max-width: 100%;
                height: auto;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to our Website!</h1>
        <img src="/static/pic.png" alt="Picture">
    </body>
    </html>
    '''

@app.route('/static/<path:path>')  # Static files
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)