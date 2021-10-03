from flask import abort, render_template
from flask_config.models import Product


def init_app(app):
    @app.route('/')
    def index():
        """doc-string"""
        products = Product.query.all()
        return render_template('index.html', products=products)

    @app.route('/product/<product_id>')
    def product(product_id):
        """doc-string"""
        product = Product.query.filter_by(id=product_id).first() or abort(
            404, 'Produto não encontrado!'
        )
        return render_template('product.html', product=product)
