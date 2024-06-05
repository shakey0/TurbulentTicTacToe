from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template, jsonify
from extensions import r
from classes.board import Board
import os, pickle


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    board = Board(6, 6)
    r.set(board.id, pickle.dumps(board), ex=3600)
    return render_template('index.html', board_data=board.board, board_id=board.id)


@app.route('/move', methods=['POST'])
def move():
    player = 'X' # player = 'X' or 'O' or any other character
    data = request.json
    board_id = data.get('board_id')
    space = data.get('space')
    board = pickle.loads(r.get(board_id))
    for y in range(board.height):
        for x in range(board.width):
            if board.board[y][x][0] == int(space):
                board.board[y][x][1] = player
                break
    print('board:', board.board)
    r.set(board.id, pickle.dumps(board), ex=3600)
    return jsonify({'success': True, 'player': player})


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
