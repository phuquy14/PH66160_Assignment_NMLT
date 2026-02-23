# product_manager.py
import json

def load_data():
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_data(products):
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def display_all_products(products):
    if not products:
        print("=> Kho hàng trống.") [cite: 112]
        return
    print("-" * 70)
    for p in products:
        print(f"ID: {p['id']} | Tên: {p['name']} | Giá: {p['price']} | SL: {p['quantity']}")
    print("-" * 70)

def add_product(products):
    print("\n--- THÊM SẢN PHẨM ---")
    new_id = f"LT{len(products) + 1:02d}" [cite: 93]
    name = input("Nhập tên: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    qty = int(input("Nhập số lượng: "))
    products.append({"id": new_id, "name": name, "brand": brand, "price": price, "quantity": qty})
    print("=> Đã thêm thành công!")
    return products

def search_product_by_name(products):
    keyword = input("Nhập tên sản phẩm cần tìm: ").lower() [cite: 107]
    results = [p for p in products if keyword in p['name'].lower()] [cite: 108, 109]
    print(f"\n--- KẾT QUẢ TÌM KIẾM ---")
    display_all_products(results)

def delete_product(products):
    """Hỏi mã sản phẩm và xóa khỏi danh sách""" [cite: 105]
    id_del = input("Nhập mã sản phẩm cần xóa: ")
    for p in products:
        if p['id'] == id_del:
            products.remove(p)
            print(f"=> Đã xóa sản phẩm {id_del}")
            return products
    print("=> Không tìm thấy mã sản phẩm để xóa.")
    return products

# Hàm này sẽ làm ở lần 7
def update_product(products): pass