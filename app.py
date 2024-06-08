from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, render_template, jsonify
from extensions import r
from classes.board import Board
from classes.player import Player
import os, pickle


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    player_1 = Player('Player 1', 'X')
    player_2 = Player('Player 2', 'O')
    board = Board(6, 6, shapes=['l_shape'], players=[player_1, player_2])
    r.set(board.id, pickle.dumps(board), ex=3600)
    return render_template('index.html', board_data=board.board, board_id=board.id)


@app.route('/move', methods=['POST'])
def move():
    data = request.json
    board_id = data.get('board_id')
    space = data.get('space')
    board = pickle.loads(r.get(board_id))
    # player = data.get('player')
    player = "X"
    result = board.move(space, player)
    # print('board:', board.board)
    r.set(board.id, pickle.dumps(board), ex=3600)
    return jsonify({'success': True, 'player': player, 'result': result})


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
