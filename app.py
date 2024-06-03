from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    if os.environ.get('APP_ENV') == 'test':
        root_dir = os.environ.get('ROOT_DIR')
        print('Current working directory:', root_dir)
        os.chdir(root_dir)
    app.run(
        host="0.0.0.0",
        debug=True,
        port=int(os.environ.get('PORT', 5000))
    )
