# product_manager.py
import json

def load_data():
    """Đọc dữ liệu từ file products.json. Xử lý nếu file không tồn tại[cite: 83, 84, 85]."""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Nếu không thấy file (lần đầu chạy), trả về danh sách rỗng[cite: 86, 87].
        return []

def save_data(product_list):
    """Lưu danh sách sản phẩm vào file products.json[cite: 88, 89, 90]."""
    try:
        with open('products.json', 'w', encoding='utf-8') as f:
            json.dump(product_list, f, ensure_ascii=False, indent=4)
        print("=> Đã lưu dữ liệu vào hệ thống.")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def display_menu():
    print("\n--- HỆ THỐNG QUẢN LÝ CỬA HÀNG POLY-LAP ---")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("0. Lưu & Thoát chương trình")
    print("------------------------------------------")

def display_all_products(product_list):
    if not product_list:
        print("\n=> Kho hàng trống[cite: 112].")
        return

    print("\n" + "="*85)
    print(f"{'Mã ID':<8} | {'Tên sản phẩm':<30} | {'Thương hiệu':<15} | {'Giá':<12} | {'SL'}")
    print("-" * 85)
    for p in product_list:
        print(f"{p['id']:<8} | {p['name']:<30} | {p['brand']:<15} | {p['price']:>12,.0f} | {p['quantity']:>2}")
    print("="*85)

def add_product(product_list):
    print("\n--- NHẬP THÔNG TIN SẢN PHẨM MỚI ---")
    new_id = f"LT{len(product_list) + 1:02d}" # Tự động tạo ID [cite: 93]
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    try:
        price = int(input("Nhập giá bán: "))
        quantity = int(input("Nhập số lượng tồn kho: "))
    except ValueError:
        print("Lỗi: Giá và số lượng phải là số nguyên!")
        return product_list

    new_product = {"id": new_id, "name": name, "brand": brand, "price": price, "quantity": quantity}
    product_list.append(new_product)
    print(f" Thêm thành công sản phẩm: {new_id}")
    return product_list

# Các hàm sau vẫn để pass cho các lần sau
def update_product(products): pass
def delete_product(products): pass
def search_product_by_name(products): pass