#write a function called linear search product that takes the list of product and a target product name as input.The function should perform a linear search to find the target product in the list and return a list of indices of a occurrence of the product if found or an empty list if the product is not found.
def linear_search_product(product_list, triggered_product):
    indices = []
    for i, product in enumerate(product_list):
        if product == triggered_product:
            indices.append(i)
    return indices
  products = ["apple", "banana", "orange", "apple", "grape"]
triggered_product = "apple"

result = linear_search_product(products, triggered_product)
print(result)  