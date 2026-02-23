# main.py
import product_manager as pm

def main():
    # Tải dữ liệu khi khởi động chương trình [cite: 116]
    products = pm.load_data()
    
    while True:
        print("\n" + "*"*10 + " QUẢN LÝ LAPTOP POLY-LAP " + "*"*10)
        print("1. Danh sách | 2. Thêm mới | 3. Cập nhật")
        print("4. Xóa sản phẩm | 5. Tìm kiếm | 0. Lưu & Thoát")
        
        choice = input("Lựa chọn của bạn: ")
        
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
            pm.save_data(products) # Lưu dữ liệu trước khi thoát [cite: 118]
            print("Dữ liệu đã được bảo lưu. Tạm biệt!")
            break
        else:
            print("=> Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()