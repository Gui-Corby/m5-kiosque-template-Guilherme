from menu import products


def calculate_tab(dict_list):
    total = 0
    for items in dict_list:
        for product in products:
            if items["_id"] == product["_id"]:
                total += product["price"] * items["amount"]
                break
    return {"subtotal": f"${round(total, 2)}"}
