from flask import Flask, render_template
from flask import request
app = Flask(__name__)
a1=""
a2=""
a3=""
# Здесь будут функции для учета прогресса пользователя и анализа успеваемости

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=["GET","POST"])
def game1():
    global a1,a2,a3
    if request.method=="GET":
        a1=""
        a2=""
        a3=""
    if request.method=="POST":
        list1 = request.form.getlist('c1')
        list2 = request.form.getlist('c2')
        list3 = request.form.getlist('c3')
        if list1 == ['a']:
            a1="Верно"
        elif len(list1)>0:
            a1="Неверно"
        if list2 == ['d']:
            a2="Верно"
        elif len(list2)>0:
            a3="Неверно"
        if list3 == ['b']:
            a3="Верно"
        elif len(list3)>0:
            a3="Неверно"
        print(list1)
        print(list2)
        print(list3)

    return render_template('game.html', game_number=1, answer1=a1, answer2=a2, answer3=a3)

@app.route('/game2')
def game2():
    return render_template('game.html', game_number=2)

@app.route('/game3')
def game3():
    return render_template('game.html', game_number=3)

@app.route('/game4')
def game4():
    return render_template('game.html', game_number=4)

@app.route('/progress')
def progress():
    # Здесь будет логика для отображения прогресса пользователя
    return render_template('progress.html')

@app.route('/index')
def indexx():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
