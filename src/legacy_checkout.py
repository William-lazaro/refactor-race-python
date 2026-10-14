
# legacy_checkout.py

from collections import Counter

ORDERS_PROCESSED = []


def calculate_subtotal(items):
    subtotal = 0

    for item in items:
        if item["qty"] > 0:
            subtotal += item["price"] * item["qty"]

    return subtotal


def calculate_discount(customer, subtotal, coupon=""):
    discount = 0

    # Desconto por tipo de cliente
    if customer["type"] == "vip":
        if subtotal >= 1000:
            discount = subtotal * 0.15
        else:
            discount = subtotal * 0.10
    elif customer["type"] == "employee":
        discount = subtotal * 0.20
    elif customer["type"] == "regular" and subtotal >= 800:
        discount = subtotal * 0.05

    # Cupons
    if coupon == "PROMO10":
        discount += subtotal * 0.10

    if coupon == "PROMO20" and subtotal >= 500:
        discount += subtotal * 0.20

    if coupon == "VIP50" and customer["type"] == "vip":
        discount += 50

    # Desconto máximo permitido
    discount = min(discount, subtotal * 0.25)

    return discount

def calculate_shipping(items, subtotal, state="MG", express=False):
    # Peso total
    weight = 0

    for item in items:
        weight += item.get("weight", 0) * item["qty"]

    # Frete grátis para pedidos a partir de 500, sem entrega expressa
    if subtotal >= 500 and not express:
        return 0

    # Cálculo do frete por estado
    if state in {"MG", "SP", "RJ", "ES"}:
        shipping = 20 + weight * 0.4
    else:
        shipping = 35 + weight * 0.6

    # Acréscimo para entrega expressa
    if express:
        shipping *= 1.8

    return shipping


def calculate_tax(value, state):
    tax_rates = {
        "MG": 0.07,
        "SP": 0.09,
        "RJ": 0.08,
        "ES": 0.07,
    }

    tax_rate = tax_rates.get(state, 0.12)

    return value * tax_rate

def find_duplicate_products(items):
    names = [item["name"] for item in items]
    counts = Counter(names)

    return list(dict.fromkeys(
        name for name in names if counts[name] > 1
    ))

def calculate_points(customer, value, shipping, tax):
    total = value + shipping + tax

    if customer["type"] == "vip":
        return int(total / 5)

    return int(total / 10)


def process_order(customer, items, coupon="", state="MG", express=False):
    # Cálculo do subtotal
    subtotal = calculate_subtotal(items)

    # Cálculo do desconto
    desconto = calculate_discount(customer, subtotal, coupon)

    # Valor após o desconto
    valor_com_desconto = subtotal - desconto


    # Cálculo do frete
    frete = calculate_shipping(items, subtotal, state, express)

    # Impostos
    imposto = calculate_tax(valor_com_desconto, state)

    # Pontos de fidelidade
    pontos = calculate_points(customer, valor_com_desconto, frete, imposto)

    # Produtos repetidos
    duplicados = find_duplicate_products(items)

    # Resultado final
    total_final = round(valor_com_desconto + frete + imposto, 2)

    resultado = {
        "customer": customer["name"],
        "subtotal": round(subtotal, 2),
        "discount": round(desconto, 2),
        "shipping": round(frete, 2),
        "tax": round(imposto, 2),
        "total": total_final,
        "points": pontos,
        "duplicate_products": duplicados
    }

    ORDERS_PROCESSED.append(resultado)

    print("Pedido processado para " + customer["name"])
    print("Subtotal:", subtotal)
    print("Desconto:", desconto)
    print("Frete:", frete)
    print("Imposto:", imposto)
    print("TOTAL:", total_final)

    return resultado
