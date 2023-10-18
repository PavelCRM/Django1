from django.shortcuts import render, get_object_or_404
from .models import Client, Product, Order
from django.utils import timezone
from .forms import ProductForm
from django.shortcuts import redirect

# CREATE

def create_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        registration_date = request.POST['registration_date']
        client = Client(name=name, email=email, phone_number=phone_number, address=address, registration_date=registration_date)
        client.save()
        return render(request, 'client_created.html', {'client': client})
    else:
        return render(request, 'create_client.html')

def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        added_date = request.POST['added_date']
        product = Product(name=name, description=description, price=price, quantity=quantity, added_date=added_date)
        product.save()
        return render(request, 'product_created.html', {'product': product})
    else:
        return render(request, 'create_product.html')

def create_order(request):
    if request.method == 'POST':
        client_id = request.POST['client']
        total_amount = request.POST['total_amount']
        order_date = request.POST['order_date']
        products = request.POST.getlist('products')
        client = get_object_or_404(Client, pk=client_id)
        order = Order(client=client, total_amount=total_amount, order_date=order_date)
        order.save()
        order.products.set(products)
        return render(request, 'order_created.html', {'order': order})
    else:
        clients = Client.objects.all()
        products = Product.objects.all()
        return render(request, 'create_order.html', {'clients': clients, 'products': products})


# READ

def view_clients(request):
    clients = Client.objects.all()
    return render(request, 'view_clients.html', {'clients': clients})

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})

def view_orders(request):
    orders = Order.objects.all()
    return render(request, 'view_orders.html', {'orders': orders})

def view_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'view_order.html', {'order': order})


# UPDATE

def update_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)

    if request.method == 'POST':
        client.name = request.POST['name']
        client.email = request.POST['email']
        client.phone_number = request.POST['phone_number']
        client.address = request.POST['address']
        client.registration_date = request.POST['registration_date']
        client.save()
        return render(request, 'client_updated.html', {'client': client})
    else:
        return render(request, 'update_client.html', {'client': client})

def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.added_date = request.POST['added_date']
        product.save()
        return render(request, 'product_updated.html', {'product': product})
    else:
        return render(request, 'update_product.html', {'product': product})


# DELETE

def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return render(request, 'client_deleted.html')

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return render(request, 'product_deleted.html')

def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return render(request, 'order_deleted.html')


def client_ordered_products(request, client_id, days):
    end_date = timezone.now()
    start_date = end_date - timezone.timedelta(days=days)
    orders = Order.objects.filter(client_id=client_id, order_date__range=(start_date, end_date))
    unique_products = set()
    
    for order in orders:
        unique_products.update(order.products.all())
    
    return render(request, 'client_ordered_products.html', {'products': unique_products})

def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'edit_product.html', {'form': form})