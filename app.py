from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/category/<name>')
def category(name):
    return render_template('category.html', category_name=name)


@app.route('/product/<name>')
def product(name):
    return render_template('product.html', product_name=name)

if __name__ == '__main__':
    app.run(debug=True)
