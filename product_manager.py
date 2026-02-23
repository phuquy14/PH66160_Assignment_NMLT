# product_manager.py
import json

def load_data():
    """Đọc dữ liệu từ file, nếu lỗi thì trả về danh sách rỗng [cite: 83, 85, 87]"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_data(products):
    """Lưu danh sách vào file JSON [cite: 88, 89, 90]"""
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def display_all_products(products):
    """Hiển thị danh sách sản phẩm dạng bảng đơn giản [cite: 110, 111]"""
    if not products:
        print("=> Kho hàng trống. [cite: 112]")
        return
    print("-" * 70)
    for p in products:
        print(f"ID: {p['id']} | Tên: {p['name']} | Giá: {p['price']} | SL: {p['quantity']}")
    print("-" * 70)

def add_product(products):
    """Thêm sản phẩm mới và tự tạo ID [cite: 91, 93, 94]"""
    print("\n--- THÊM SẢN PHẨM ---")
    new_id = f"LT{len(products) + 1:02d}"
    name = input("Nhập tên: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    qty = int(input("Nhập số lượng: "))
    
    products.append({"id": new_id, "name": name, "brand": brand, "price": price, "quantity": qty})
    print("=> Đã thêm thành công!")
    return products

def search_product_by_name(products):
    """Tìm kiếm sản phẩm theo tên (không phân biệt hoa thường) [cite: 106, 109]"""
    keyword = input("Nhập tên sản phẩm cần tìm: ").lower() # [cite: 107]
    results = []
    
    for p in products:
        if keyword in p['name'].lower(): # Kiểm tra từ khóa có trong tên không [cite: 108]
            results.append(p)
            
    print(f"\n--- KẾT QUẢ TÌM KIẾM CHO '{keyword}' ---")
    display_all_products(results)

# Các hàm này sẽ làm ở lần 6, 7
def update_product(products): pass
def delete_product(products): pass