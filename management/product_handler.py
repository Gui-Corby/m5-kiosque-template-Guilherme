from menu import products


def get_product_by_id(number):
    if not isinstance(number, int):
        raise TypeError("product id must be an int")
    for product in products:
        if product["_id"] == number:
            return product
    return {}


def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    products_list = []
    for product in products:
        if product["type"] == type:
            products_list.append(product)
    return products_list


def add_product(menu, **kwargs):
    counter = 0
    if len(menu) == 0:
        kwargs["_id"] = counter + 1
        menu.append(kwargs)
    else:
        for product in menu:
            if product["_id"] > counter:
                counter = product["_id"]
        kwargs["_id"] = counter = counter + 1
        menu.append(kwargs)
    return kwargs


def add_product_extra(menu, *args, **kwargs):
    for required_key in args:
        if required_key not in kwargs:
            raise KeyError(f"field {required_key} is required")
    for field in list(kwargs):
        if field not in args:
            kwargs.pop(field)
    counter = 0
    if len(menu) == 0:
        kwargs["_id"] = counter + 1
        menu.append(kwargs)
    else:
        for product in menu:
            if product["_id"] > counter:
                counter = product["_id"]
        kwargs["_id"] = counter = counter + 1
        menu.append(kwargs)
    return kwargs


def menu_report():
    product_count = len(products)
    price = 0
    for product in products:
        price += product["price"]
    average_price = price / product_count
    count_type = {}
    for product in products:
        type = product["type"]
        if type in count_type:
            count_type[type] += 1
        else:
            count_type[type] = 1
    most_common_type = max(count_type, key=count_type.get)
    return f"Products Count: {product_count} - Average Price: ${average_price:.1f} - Most Common Type: {most_common_type}"
