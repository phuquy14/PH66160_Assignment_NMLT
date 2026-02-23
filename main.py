# main.py
import product_manager

def main():
    while True:
        # Gọi hàm hiển thị menu từ module manager
        product_manager.display_menu()
        
        choice = input("Mời bạn chọn chức năng (0-5): ")
        
        if choice == '1':
            print("\n[Tính năng hiển thị đang được phát triển...]")
        elif choice == '2':
            print("\n[Tính năng thêm sản phẩm đang được phát triển...]")
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