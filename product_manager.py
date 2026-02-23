# product_manager.py

# Danh sách sản phẩm khởi tạo (có thể để trống hoặc giữ lại data mẫu)
products = [
    {"id": "LT01", "name": "Laptop Gaming Acer Nitro 5", "brand": "Acer", "price": 18000000, "quantity": 10},
    {"id": "LT02", "name": "MacBook Air M2", "brand": "Apple", "price": 25000000, "quantity": 5}
]

def display_menu():
    print("\n--- HỆ THỐNG QUẢN LÝ CỬA HÀNG POLY-LAP ---")
    print("1. Xem danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật sản phẩm")
    print("4. Xóa sản phẩm")
    print("5. Tìm kiếm sản phẩm")
    print("0. Thoát chương trình")
    print("------------------------------------------")

def display_all_products(product_list):
    if not product_list:
        print("\n=> Kho hàng trống.")
        return

    print("\n" + "="*85)
    print(f"{'Mã ID':<8} | {'Tên sản phẩm':<30} | {'Thương hiệu':<15} | {'Giá':<12} | {'SL'}")
    print("-" * 85)
    for p in product_list:
        print(f"{p['id']:<8} | {p['name']:<30} | {p['brand']:<15} | {p['price']:>12,.0f} | {p['quantity']:>2}")
    print("="*85)

def add_product(product_list):
    """Hỏi người dùng nhập thông tin và thêm sản phẩm mới vào danh sách"""
    print("\n--- NHẬP THÔNG TIN SẢN PHẨM MỚI ---")
    
    # Tự động tạo mã sản phẩm dựa trên số lượng hiện tại (LT + số thứ tự) 
    new_id = f"LT{len(product_list) + 1:02d}"
    
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    
    # Chuyển đổi giá và số lượng sang kiểu số nguyên [cite: 73, 74]
    try:
        price = int(input("Nhập giá bán: "))
        quantity = int(input("Nhập số lượng tồn kho: "))
    except ValueError:
        print("Lỗi: Giá và số lượng phải là số nguyên!")
        return product_list

    # Tạo dictionary sản phẩm mới [cite: 94]
    new_product = {
        "id": new_id,
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }
    
    product_list.append(new_product)
    print(f" Thêm thành công sản phẩm: {new_id}")
    return product_list # Trả về danh sách đã cập nhật [cite: 99]

# Các hàm sau vẫn tạm để pass để hoàn thiện ở các lần tiếp theo
def load_data(): pass
def save_data(products): pass
def update_product(products): pass
def delete_product(products): pass
def search_product_by_name(products): pass