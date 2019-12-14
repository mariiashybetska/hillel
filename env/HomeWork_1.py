from flask import Flask
from faker import Faker
import requests


app = Flask('app')


@app.route('/')
def title():
    return 'My first home work'


@app.route('/requirements')
def get_requirements():
    with open('requirements.txt') as r:
        requirements = r.read()
    return requirements


@app.route('/fake_names')
def get_fake_names():
    fake = Faker()
    return '<br>'.join (
        f'name: {fake.name()}, email: {fake.email()}' for i in range(100)
    )


@app.route('/avg_metrics')
def avg_metrics():
    with open('hw.csv') as f:
        content = f.read()
        content = content.split('\n')[1::]
        number_of_records = 0
        sum_of_h = 0
        sum_of_w = 0

        for row in content:
            if not row:
                continue
            number_of_records += 1
            h = float(row.split(',')[1])
            w = float(row.split(',')[2])
            sum_of_h += h
            sum_of_w += w

        avg_h = round(sum_of_h / number_of_records * 2.54, 2)
        avg_w = round(sum_of_w / number_of_records * 0.454, 2)
    return f'Average height: {avg_h} and average weight {avg_w}'


@app.route('/astronauts_online')
def get_cosmo_online():
    res = requests.get('http://api.open-notify.org/astros.json')
    json_ = res.json()
    number_of_astro = json_['number']
    return f'There are {number_of_astro} astronauts in space right now'


if __name__ == '__main__':
    app.run(port=5001)