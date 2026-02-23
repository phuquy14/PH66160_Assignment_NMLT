# product_manager.py
import json

def load_data():
    """Đọc dữ liệu từ file products.json[cite: 84]. Xử lý nếu file chưa tồn tại[cite: 85, 87]."""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(products):
    """Ghi danh sách sản phẩm vào file JSON[cite: 89, 90]."""
    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def get_int_input(prompt):
    """Hàm phụ để đảm bảo người dùng nhập đúng số nguyên[cite: 130, 135]."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("=> Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

def display_all_products(products):
    """Hiển thị toàn bộ sản phẩm ngay ngắn[cite: 111]."""
    if not products:
        print("\n=> Kho hàng trống[cite: 112].")
        return
    print("\n" + "="*70)
    print(f"{'ID':<6} | {'Tên sản phẩm':<25} | {'Thương hiệu':<12} | {'Giá':>10}")
    print("-" * 70)
    for p in products:
        # Định dạng hiển thị tên tối đa 25 ký tự để bảng không bị vỡ [cite: 111]
        name = (p['name'][:22] + '..') if len(p['name']) > 25 else p['name']
        print(f"{p['id']:<6} | {name:<25} | {p['brand']:<12} | {p['price']:>10,}đ")
    print("="*70)

def add_product(products):
    """Thêm sản phẩm mới với ID tự động[cite: 91, 93]."""
    print("\n--- THÊM SẢN PHẨM MỚI ---")
    new_id = f"LT{len(products) + 1:02d}"
    name = input("Nhập tên: ")
    brand = input("Nhập thương hiệu: ")
    price = get_int_input("Nhập giá: ")
    qty = get_int_input("Nhập số lượng: ")
    
    products.append({"id": new_id, "name": name, "brand": brand, "price": price, "quantity": qty})
    print(f"=> Đã thêm thành công sản phẩm {new_id}!")
    return products

def search_product_by_name(products):
    """Tìm kiếm không phân biệt hoa thường[cite: 108, 109]."""
    keyword = input("Nhập từ khóa tìm kiếm: ").lower()
    results = [p for p in products if keyword in p['name'].lower()]
    print(f"\nKết quả tìm kiếm cho: '{keyword}'")
    display_all_products(results)

def delete_product(products):
    """Xóa sản phẩm theo mã ID[cite: 105]."""
    id_del = input("Nhập mã cần xóa: ").upper()
    new_list = [p for p in products if p['id'] != id_del]
    if len(new_list) < len(products):
        print(f"=> Đã xóa thành công {id_del}!")
        return new_list
    print("=> Không tìm thấy mã sản phẩm.")
    return products

def update_product(products):
    """Cập nhật thông tin sản phẩm có sẵn[cite: 100, 103]."""
    id_up = input("Nhập mã cần sửa: ").upper()
    for p in products:
        if p['id'] == id_up:
            print(f"Sửa thông tin cho {id_up}:")
            p['name'] = input(f"Tên mới ({p['name']}): ") or p['name']
            p['brand'] = input(f"Thương hiệu mới ({p['brand']}): ") or p['brand']
            p['price'] = get_int_input("Giá mới: ")
            p['quantity'] = get_int_input("Số lượng mới: ")
            print("=> Cập nhật hoàn tất!")
            return products
    print("=> Không tìm thấy mã sản phẩm.")
    return products