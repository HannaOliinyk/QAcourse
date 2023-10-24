import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)
    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    #Check quantity of orders equal to 1
    assert len(orders) == 2
    #Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

@pytest.mark.database
def test_customer_insert():
    db = Database()
    db.insert_new_customer(customer_id = 3, name = 'Ivan', address = 'Peremogy street, 43', \
                           city = 'Dnipro', postalCode = 49000, country = 'Ukraine')
    print("Новий клієнт був успішно доданий")

@pytest.mark.database
def test_update_change_of_contact_information():
    db = Database()
    user_Ivan = db.update_change_of_contact_information('Poltava', 3)
    print(user_Ivan)

@pytest.mark.database
def test_update_product_with_negative_quantity():
    db = Database()
    with pytest.raises(ValueError):
        db.update_product_qnt_by_id(product_id = 2, qnt = -5)
    products_with_negative_quantity = db.get_products_with_negative_quantity()
    assert len(products_with_negative_quantity) == 1

@pytest.mark.database
def test_add_new_order():
    db = Database()
    new_order = db.add_new_order(id = 2, customer_id = 3, product_id = 4, order_date = '14:15:28')
    print(new_order)

@pytest.mark.database
def test_add_new_order_without_product():
    db = Database()
    with pytest.raises(ValueError, match = "Invalid product_id"):
        db.add_new_order(id = 3, customer_id = 3, product_id = None, order_date = '14:15:50')