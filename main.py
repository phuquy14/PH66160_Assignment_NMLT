# main.py
import product_manager as pm

def main():
    # Tải dữ liệu khi mở app [cite: 116]
    products = pm.load_data()
    
    while True:
        print("\n1. Xem | 2. Thêm | 3. Sửa | 4. Xóa | 5. Tìm | 0. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '5':
            pm.search_product_by_name(products) # Gọi hàm tìm kiếm [cite: 114]
        elif choice == '0':
            pm.save_data(products) # Lưu trước khi thoát [cite: 118]
            print("Đã lưu và thoát!")
            break
        else:
            print("Chưa phát triển hoặc chọn sai!")

if __name__ == "__main__":
    main()