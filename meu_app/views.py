from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from meu_app.forms import ProductForm, SignUpForm
from meu_app.models import Product


def index(request):

    return render(request, "index.html")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário cadastrado com sucesso! Faça login para continuar.")

            return redirect("login")

    else:
        form = SignUpForm()

    return render(request, "signup.html", {"form": form})


@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, "Você saiu do sistema.")

    return redirect("index")


@login_required
def product_list(request):
    search = request.GET.get("search", "").strip()
    order = request.GET.get("order", "asc")
    products = Product.objects.filter(active=True)

    if search:
        products = products.filter(name__icontains=search)

    if order == "desc":
        products = products.order_by(Lower("name").desc())

    else:
        order = "asc"
        products = products.order_by(Lower("name"))

    context = {"products": products, "search": search, "order": order}

    return render(request, "product_list.html", context)


@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()
            messages.success(request, f"Produto \"{product.name}\" cadastrado com sucesso!")

            return redirect("product_list")

    else:
        form = ProductForm()

    return render(request, "product_create.html", {"form": form})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk, active=True)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            product = form.save()
            messages.success(request, f"Produto \"{product.name}\" editado com sucesso!")

            return redirect("product_list")

    else:
        form = ProductForm(instance=product)

    return render(request, "product_update.html", {"form": form, "product": product})


@login_required
@require_POST
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk, active=True)
    product.active = False
    product.save()
    messages.success(request, f"Produto \"{product.name}\" desativado com sucesso!")

    return redirect("product_list")
