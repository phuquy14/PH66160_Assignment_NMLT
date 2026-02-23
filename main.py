# main.py
import product_manager

def main():
    # Tải dữ liệu ngay khi bắt đầu chương trình [cite: 116]
    products = product_manager.load_data()
    
    while True:
        product_manager.display_menu()
        choice = input("Mời bạn chọn chức năng (0-5): ")
        
        if choice == '1':
            product_manager.display_all_products(products)
            
        elif choice == '2':
            products = product_manager.add_product(products)
            
        elif choice == '3':
            print("\n[Tính năng cập nhật đang được phát triển...]")
        elif choice == '4':
            print("\n[Tính năng xóa sản phẩm đang được phát triển...]")
        elif choice == '5':
            print("\n[Tính năng tìm kiếm đang được phát triển...]")
            
        elif choice == '0':
            # Lưu dữ liệu trước khi thoát [cite: 118]
            product_manager.save_data(products)
            print("Cảm ơn bạn đã sử dụng phần mềm POLY-LAP. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()