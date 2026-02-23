# main.py
import product_manager as pm

def main():
    products = pm.load_data()
    
    while True:
        print("\n--- QUẢN LÝ POLY-LAP ---")
        print("1. Xem | 2. Thêm | 3. Sửa | 4. Xóa | 5. Tìm | 0. Thoát")
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            pm.display_all_products(products)
        elif choice == '2':
            products = pm.add_product(products)
        elif choice == '3':
            products = pm.update_product(products) # Kích hoạt chức năng sửa
        elif choice == '4':
            products = pm.delete_product(products)
        elif choice == '5':
            pm.search_product_by_name(products)
        elif choice == '0':
            pm.save_data(products)
            print("Đã lưu. Tạm biệt!")
            break
        else:
            print("Lựa chọn sai, vui lòng nhập lại!")

if __name__ == "__main__":
    main()