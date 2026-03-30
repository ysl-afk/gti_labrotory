from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        p = float(request.form.get('principal'))
        i = float(request.form.get('rate'))
        n = int(request.form.get('time'))

        total = p * (1 + i / 100) ** n

        result = f"Через {n} лет итоговая сумма составит: {total:.2f} руб."

    except Exception as e:
        result = f"Ошибка: проверьте введенные данные!"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)