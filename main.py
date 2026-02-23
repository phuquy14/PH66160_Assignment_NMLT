# main.py
import product_manager

def main():
    while True:
        product_manager.display_menu()
        choice = input("Mời bạn chọn chức năng (0-5): ")
        
        if choice == '1':
            # Gọi hàm hiển thị và truyền vào danh sách products [cite: 110]
            product_manager.display_all_products(product_manager.products)
        elif choice == '2':
            print("\n[Tính năng thêm sản phẩm đang được phát triển...]")
        # ... (các lựa chọn khác giữ nguyên như lần 1)
        elif choice == '0':
            print("Cảm ơn bạn đã sử dụng phần mềm POLY-LAP. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()