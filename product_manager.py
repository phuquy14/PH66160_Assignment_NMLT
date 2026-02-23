# product_manager.py
# Module quản lý các hàm nghiệp vụ cho cửa hàng POLY-LAP [cite: 82]
import json

def load_data():
    """Đọc dữ liệu từ file products.json, trả về danh sách trống nếu file lỗi [cite: 83-87]"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] # Trả về list rỗng nếu lần đầu chạy [cite: 85-86]

def save_data(products):
    """Lưu danh sách sản phẩm vào file định dạng JSON [cite: 88-90]"""
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def get_int_input(prompt):
    """Kiểm tra tính hợp lệ của số nguyên nhập vào [cite: 132]"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("=> Lỗi: Dữ liệu phải là số nguyên!")

def display_all_products(products):
    """Hiển thị toàn bộ kho hàng dưới dạng bảng [cite: 110-112]"""
    if not products:
        print("\n=> Kho hàng trống.")
        return
    print("\n" + "="*70)
    print(f"{'ID':<6} | {'Tên sản phẩm':<25} | {'Thương hiệu':<12} | {'Giá':>10}")
    print("-" * 70)
    for p in products:
        # Giới hạn độ dài tên để bảng không bị lệch [cite: 111]
        name = (p['name'][:22] + '..') if len(p['name']) > 25 else p['name']
        print(f"{p['id']:<6} | {name:<25} | {p['brand']:<12} | {p['price']:>10,}đ")
    print("="*70)

def add_product(products):
    """Thêm sản phẩm và tự động tạo mã ID (LT01, LT02,...) [cite: 91-94, 134]"""
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    new_id = f"LT{len(products) + 1:02d}"
    name = input("Nhập tên laptop: ")
    brand = input("Nhập thương hiệu: ")
    price = get_int_input("Nhập giá: ")
    qty = get_int_input("Nhập số lượng tồn kho: ")
    
    products.append({
        "id": new_id, "name": name, "brand": brand, 
        "price": price, "quantity": qty
    })
    print(f"=> Đã thêm thành công sản phẩm {new_id}!")
    return products

def search_product_by_name(products):
    """Tìm kiếm sản phẩm theo từ khóa (không phân biệt hoa/thường) [cite: 106-109]"""
    keyword = input("Nhập tên laptop cần tìm: ").lower()
    # Sử dụng List Comprehension để lọc dữ liệu [cite: 133]
    results = [p for p in products if keyword in p['name'].lower()]
    print(f"\nKết quả tìm kiếm cho từ khóa: '{keyword}'")
    display_all_products(results)

def delete_product(products):
    """Xóa sản phẩm theo mã ID [cite: 104-105]"""
    id_del = input("Nhập mã ID cần xóa (VD: LT01): ").upper()
    # Lọc ra danh sách mới không chứa ID cần xóa
    new_list = [p for p in products if p['id'] != id_del]
    if len(new_list) < len(products):
        print(f"=> Đã xóa thành công {id_del}!")
        return new_list
    print("=> Không tìm thấy mã sản phẩm để xóa.")
    return products

def update_product(products):
    """Cập nhật thông tin chi tiết của sản phẩm theo ID [cite: 100-103]"""
    id_up = input("Nhập mã ID cần cập nhật: ").upper()
    for p in products:
        if p['id'] == id_up:
            print(f"Cập nhật thông tin cho {id_up}:")
            p['name'] = input(f"Tên mới ({p['name']}): ") or p['name']
            p['brand'] = input(f"Thương hiệu mới ({p['brand']}): ") or p['brand']
            p['price'] = get_int_input("Giá mới: ")
            p['quantity'] = get_int_input("Số lượng mới: ")
            print("=> Cập nhật thành công!")
            return products
    print("=> Không tìm thấy mã ID phù hợp.")
    return products