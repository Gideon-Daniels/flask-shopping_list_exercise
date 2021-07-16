from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('/shoppinglist.html')


@app.route('/showitems', methods=['POST'])
def showitems():
    item_name = request.form['name']
    item_id = request.form['id']
    quantity = request.form['quantity']
    price = request.form['price']
    total = int(price)*int(quantity)
    return render_template('/showitems.html',
                           item_name=item_name,
                           item_id=item_id,
                           quantity=quantity,
                           price=price,
                           total=total
                           )


if __name__ == '__main__':
    app.debug = True
    app.run()
