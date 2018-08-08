from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
	fav_players = ["player1","player2","player3","player45"]
	return render_template("index.html",likes_same_sports=False,list1=fav_players)

if __name__ == '__main__':
   app.run(debug = True)