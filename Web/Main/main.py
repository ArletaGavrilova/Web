import random
import os
import os.path
facts_list = ['1. Всего существует 33 основных кошачьих породы. А количество домашних кошек в мире достигает 500 миллионов.', 
              '2. Частота пульса у кошки гораздо выше, чем у человека и составляет от 110 до 140 ударов сердца в минуту.',
              '3. В среднем кошки весят около пяти килограммов, а вот кошки Сингапурской породы – всего два с небольшим килограмма.' ]

image_dir = os.path.join(os.path.dirname(images), images)
if not os.path.exists(image_dir):
    os.wakedirs(image_dir)

for images_list in ['mem1', 'mem2', 'mem3', 'mem4', 'mem5']
    image_path = os.path.join(image_dir,)
    with open (image_path,'wb') as f:
        f.write(image_data)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ''' <h1>Привет!</h1>
        <a href="/random_fact">Посмотреть случайный факт!</a>'''

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/puti")
def images():
    return ''' <h1>Тут случайная картинка!</h1>
        <a href="/random_images">Посмотреть случайную картинку!</a>'''

@app.route("/random_images")
def random_images():
    return f' <p>{random.choice(images_list)}</p>'


app.run(debug=True)