# main.py
import product_manager as pm

def main():
    products = pm.load_data() [cite: 116]
    
    while True: [cite: 117]
        print("\n1. Xem | 2. Thêm | 3. Sửa | 4. Xóa | 5. Tìm | 0. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '4':
            products = pm.delete_product(products) # Gọi hàm xóa
        elif choice == '5':
            pm.search_product_by_name(products)
        elif choice == '0':
            pm.save_data(products) [cite: 118]
            print("Đã lưu và thoát!")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()