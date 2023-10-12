from django.shortcuts import render
from .models import Client, Product, Order
from datetime import datetime, timedelta

# Клиенты

def create_client(name, email, phone_number, address, registration_date):
    """
    Создает нового клиента и возвращает его.
    """
    client = Client.objects.create(
        name=name,
        email=email,
        phone_number=phone_number,
        address=address,
        registration_date=registration_date
    )
    return client

def get_client_by_id(client_id):
    """
    Возвращает клиента по его ID, если такой существует. Иначе возвращает None.
    """
    try:
        client = Client.objects.get(id=client_id)
        return client
    except Client.DoesNotExist:
        return None

def update_client(client_id, name=None, email=None, phone_number=None, address=None, registration_date=None):
    """
    Обновляет данные клиента по его ID. Возвращает обновленного клиента или None, если клиент не найден.
    """
    client = get_client_by_id(client_id)
    if client is not None:
        if name is not None:
            client.name = name
        if email is not None:
            client.email = email
        if phone_number is not None:
            client.phone_number = phone_number
        if address is not None:
            client.address = address
        if registration_date is not None:
            client.registration_date = registration_date
        client.save()
        return client
    return None

def delete_client(client_id):
    """
    Удаляет клиента по его ID. Возвращает True, если клиент был успешно удален, иначе False.
    """
    client = get_client_by_id(client_id)
    if client is not None:
        client.delete()
        return True
    return False

# Аналогичные функции для работы с товарами и заказами...

# Товары

def create_product(name, description, price, quantity, added_date):
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        added_date=added_date
    )
    return product

def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        return product
    except Product.DoesNotExist:
        return None

def update_product(product_id, name=None, description=None, price=None, quantity=None, added_date=None):
    product = get_product_by_id(product_id)
    if product is not None:
        if name is not None:
            product.name = name
        if description is not None:
            product.description = description
        if price is not None:
            product.price = price
        if quantity is not None:
            product.quantity = quantity
        if added_date is not None:
            product.added_date = added_date
        product.save()
        return product
    return None

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product is not None:
        product.delete()
        return True
    return False

# Заказы

def create_order(client, products, total_amount, order_date):
    order = Order.objects.create(
        client=client,
        total_amount=total_amount,
        order_date=order_date
    )
    order.products.set(products)
    return order

def get_order_by_id(order_id):
    try:
        order = Order.objects.get(id=order_id)
        return order
    except Order.DoesNotExist:
        return None

def update_order(order_id, client=None, products=None, total_amount=None, order_date=None):
    order = get_order_by_id(order_id)
    if order is not None:
        if client is not None:
            order.client = client
        if products is not None:
            order.products.set(products)
        if total_amount is not None:
            order.total_amount = total_amount
        if order_date is not None:
            order.order_date = order_date
        order.save()
        return order
    return None

def delete_order(order_id):
    order = get_order_by_id(order_id)
    if order is not None:
        order.delete()
        return True
    return False


def client_ordered_products(request, client_id):
    client = Client.objects.get(id=client_id)

    # Определите даты начала и конца периодов
    today = datetime.now()
    one_week_ago = today - timedelta(days=7)
    one_month_ago = today - timedelta(days=30)
    one_year_ago = today - timedelta(days=365)

    # Получите все заказы клиента за разные периоды
    orders_7_days = Order.objects.filter(client=client, order_date__gte=one_week_ago)
    orders_30_days = Order.objects.filter(client=client, order_date__gte=one_month_ago)
    orders_365_days = Order.objects.filter(client=client, order_date__gte=one_year_ago)

    # Соберите все товары из этих заказов
    products_7_days = []
    products_30_days = []
    products_365_days = []

    for order in orders_7_days:
        products_7_days.extend(order.products.all())

    for order in orders_30_days:
        products_30_days.extend(order.products.all())

    for order in orders_365_days:
        products_365_days.extend(order.products.all())

    # Уберите дубликаты товаров
    products_7_days = list(set(products_7_days))
    products_30_days = list(set(products_30_days))
    products_365_days = list(set(products_365_days))

    return render(request, 'client_ordered_products.html', {
        'products_7_days': products_7_days,
        'products_30_days': products_30_days,
        'products_365_days': products_365_days
    })