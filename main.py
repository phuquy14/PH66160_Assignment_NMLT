# main.py
import product_manager

def main():
    while True:
        product_manager.display_menu()
        choice = input("Mời bạn chọn chức năng (0-5): ")
        
        if choice == '1':
            product_manager.display_all_products(product_manager.products)
            
        elif choice == '2':
            # Cập nhật lại danh sách sau khi thêm mới
            product_manager.products = product_manager.add_product(product_manager.products)
            
        elif choice == '3':
            print("\n[Tính năng cập nhật đang được phát triển...]")
        elif choice == '4':
            print("\n[Tính năng xóa sản phẩm đang được phát triển...]")
        elif choice == '5':
            print("\n[Tính năng tìm kiếm đang được phát triển...]")
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng phần mềm POLY-LAP. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()