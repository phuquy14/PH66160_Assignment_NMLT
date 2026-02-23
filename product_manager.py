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
        print("=> Kho hàng trống.")
        return
    print("-" * 75)
    for p in products:
        print(f"ID: {p['id']} | {p['name'][:20]:<20} | {p['price']:>10}đ | SL: {p['quantity']}")
    print("-" * 75)

def add_product(products):
    print("\n--- THÊM SẢN PHẨM ---")
    # Tạo ID duy nhất bằng cách cộng 1 vào độ dài [cite: 93]
    new_id = f"LT{len(products) + 1:02d}"
    name = input("Nhập tên: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    qty = int(input("Nhập số lượng: "))
    products.append({"id": new_id, "name": name, "brand": brand, "price": price, "quantity": qty})
    return products

def search_product_by_name(products):
    keyword = input("Nhập tên sản phẩm cần tìm: ").lower()
    # Tìm kiếm không phân biệt hoa thường [cite: 108, 109]
    results = [p for p in products if keyword in p['name'].lower()]
    display_all_products(results)

def delete_product(products):
    """SỬA LỖI: Dùng list comprehension để lọc bỏ phần tử cần xóa"""
    id_del = input("Nhập mã sản phẩm cần xóa: ")
    len_before = len(products)
    products = [p for p in products if p['id'] != id_del]
    
    if len(products) < len_before:
        print(f"=> Đã xóa thành công {id_del}!")
    else:
        print("=> Không tìm thấy mã sản phẩm.")
    return products

def update_product(products):
    """HÀM MỚI: Cập nhật thông tin sản phẩm [cite: 100]"""
    id_up = input("Nhập mã sản phẩm cần sửa: ")
    for p in products:
        if p['id'] == id_up:
            print(f"Đang sửa: {p['name']}")
            p['name'] = input("Tên mới: ")
            p['brand'] = input("Thương hiệu mới: ")
            p['price'] = int(input("Giá mới: "))
            p['quantity'] = int(input("Số lượng mới: "))
            print("=> Cập nhật thành công!")
            return products
    print("=> Không tìm thấy mã sản phẩm để sửa.")
    return products