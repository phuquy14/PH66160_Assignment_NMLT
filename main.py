# main.py
# Chương trình chính điều khiển ứng dụng POLY-LAP [cite: 115]
import product_manager as pm

def main():
    # Bước 1: Tải dữ liệu từ file khi khởi động [cite: 116]
    products = pm.load_data()
    
    while True:
        # Bước 2: Hiển thị menu chức năng [cite: 117]
        print("\n" + "*"*10 + " POLY-LAP MANAGER " + "*"*10)
        print("1. Xem danh sách | 2. Thêm mới | 3. Cập nhật")
        print("4. Xóa sản phẩm  | 5. Tìm kiếm | 0. Lưu & Thoát")
        
        choice = input("Lựa chọn chức năng: ")
        
        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '3':
            products = pm.update_product(products)
        elif choice == '4':
            products = pm.delete_product(products)
        elif choice == '5':
            pm.search_product_by_name(products)
        elif choice == '0':
            # Bước 3: Lưu lại toàn bộ thay đổi trước khi thoát [cite: 118]
            pm.save_data(products)
            print("Dữ liệu đã được lưu an toàn. Tạm biệt!")
            break
        else:
            print("=> Lựa chọn không hợp lệ, vui lòng thử lại!")

if __name__ == "__main__":
    main()
# hh