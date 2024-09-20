from flask import Flask,render_template,request,redirect,url_for
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result/<int:price>')
def result(price):
    return render_template('result.html', price=price, accuracy=94.17)

@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        car_model = request.form['carModel']
        mileage = int(request.form['mileage'])
        car_age = int(request.form['age'])

        a = 0
        b=0
        if car_model == 'BMW X5':
            a = 1
        elif car_model == 'Mercedez Benz C class':
            b = 1
        else:
            pass

    with open('model_pickle','rb') as f:
        model = pickle.load(f)

    predicted_price = model.predict([[mileage,car_age,a,b]])

    return redirect(url_for('result',price=predicted_price))

if __name__=='__main__':
    app.run(debug=True)