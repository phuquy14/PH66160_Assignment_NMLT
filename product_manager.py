# product_manager.py

# Khởi tạo danh sách sản phẩm với một vài dữ liệu mẫu để chạy thử 
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
    """Hiển thị toàn bộ sản phẩm trong kho một cách ngay ngắn [cite: 110, 111]"""
    if not product_list:
        print("\n=> Kho hàng trống. [cite: 112]")
        return

    print("\n" + "="*85)
    print(f"{'Mã ID':<8} | {'Tên sản phẩm':<30} | {'Thương hiệu':<15} | {'Giá':<12} | {'SL'}")
    print("-" * 85)
    
    for p in product_list:
        # Hiển thị thông tin từng sản phẩm theo cột [cite: 111]
        print(f"{p['id']:<8} | {p['name']:<30} | {p['brand']:<15} | {p['price']:>12,.0f} | {p['quantity']:>2}")
    print("="*85)

# Khai báo sẵn khung các hàm sẽ làm trong các lần tiếp theo [cite: 82]
def load_data(): pass
def save_data(products): pass
def add_product(products): pass
def update_product(products): pass
def delete_product(products): pass
def search_product_by_name(products): pass