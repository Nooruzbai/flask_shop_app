from flask import Blueprint, session, flash, redirect, url_for, render_template, request
from flask_login import current_user

from source.cart_app.utils import counting_total_for_cart_items
from source.item_app.item_models import Item

cart = Blueprint('cart', __name__)


@cart.route('/cart_list')
def cart_list():
    if 'cart' not in session or not session['cart']:
        flash('Your cart is empty', category='warning')
        return render_template('cart/cart.html', user=current_user)
    total = counting_total_for_cart_items(session["cart"])
    return render_template('cart/cart.html', user=current_user, total=total)


@cart.route("/add_cart/<int:pk>", methods=['POST'])
def add_cart(pk):
    item = Item.query.get_or_404(pk)
    items_dictionary = {
        str(pk): {'name': item.name, 'quantity': str(1), 'price': str(item.price)},
    }
    if 'cart' in session:
        if str(pk) in session['cart']:
            flash(f"{item.name} is already in cart", category='warning')
        session['cart'].update(items_dictionary)
        session.modified = True
    else:
        session['cart'] = items_dictionary
    return redirect(url_for('cart.cart_list'))


@cart.route("/delete_item_from_cart/<int:pk>", methods=['POST'])
def delete_item_from_cart(pk):
    for item_id, item in list(session['cart'].items()):
        if int(item_id) == pk:
            session['cart'].pop(item_id)
            session.modified = True
    return redirect(url_for('cart.cart_list'))


@cart.route("/update_item_in_cart/<int:pk>", methods=['POST'])
def update_item_in_cart(pk):
    # for item_id, item in list(session['cart'].items()):
    #     if int(item_id) == pk:
    #         session['cart'].pop(item_id)
    #         session.modified = True
    # return redirect(url_for('cart.cart_list'))
    pass




