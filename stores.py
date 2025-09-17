def input_price(prompt: str) -> float | None:
    while True:
        user_input = input(prompt)
        try:
            price = float(user_input)
            if price <= 0:
                print("Цена должна быть положительной.")
                continue
            return price
        except ValueError:
            print("Ошибка: введите число, например 1.25")

# Создан класс магазинов
class Store:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.items: dict[str, float] = {} # пустой словарь

    # Добавляет товар в ассортимент или обновляет цену
    def add_item(self, item_name: str, price: float ) -> None:
        self.items[item_name] = price

    # Возвращает цену товара по названию или None, если товар отсутствует
    def get_price(self, item_name: str) -> float | None:
        return self.items.get(item_name)

    # Удаляет товар из ассортимента. Возвращает True, если удалено, иначе False.
    def remove_item(self, item_name: str) -> bool:

        if item_name in self.items:
            del self.items[item_name]
            return True
        return False

    # Обновляет цену товара. Возвращает True, если товар найден и обновлён, иначе False.
    def update_price(self, item_name: str, new_price: float) -> bool:
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной")
        if item_name in self.items:
            self.items[item_name] = new_price
            return True
        return False

    def list_items(self) -> None:
        print(f"\n Ассортимент магазина '{self.name}':")
        if not self.items:
            print("- нет товаров. ")
        for item, price in self.items.items():
            print(f"- {item}: {price: .2f} руб.")

class StoreManager:
    def __init__(self):
        self.stores: list[Store] = []

    def add_store(self, new_store: Store) -> None:
        self.stores.append(new_store)

    # Ищем магазин с самой низкой ценой
    def find_cheapest(self, item_name: str) -> tuple[str, float] | None:
        cheapest: tuple[str, float] | None = None
        for current_store in self.stores:
            price = current_store.get_price(item_name)
            if price is not None:
                if cheapest is None or price < cheapest[1]:
                    cheapest = (current_store.name, price)
        return cheapest

    def list_all_stores(self) -> None:
        print("\n Список всех магазиновЖ")
        for store in self.stores:
            print(f"- {store.name} ({store.address})")

store1 = Store("Чайный", "ул. Тенистая, 75Е")
store1.add_item("яблоки", 0.5)
store1.add_item("молоко", 1.2)

store2 = Store("Кофейный дворик", "ул. Наличная, 34")
store2.add_item("молоко", 1.1)
store2.add_item("слива", 0.69)

store3 = Store("Фруктовый", "пл. Дубовая, 2Б")
store3.add_item("бананы", 0.75)
store3.add_item("слива", 0.65)

manager = StoreManager()
manager.add_store(store1)
manager.add_store(store2)
manager.add_store(store3)

def run_store_interface(current_store):
    while True:
        print("\nВыберите действие:")
        print("1 — Добавить товар")
        print("2 — Обновить цену")
        print("3 — Удалить товар")
        print("4 — Показать ассортимент")
        print("5 — Узнать цену товара")
        print("0 — Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            user_item_name = input("Название товара: ")
            user_item_price = input_price("Цена: ")
            current_store.add_item(user_item_name, user_item_price)
            print("Товар добавлен.")

        elif choice == "2":
            user_item_name = input("Название товара: ")
            price = input_price("Новая цена: ")
            try:
                if current_store.update_price(user_item_name, price):
                    print("Цена обновлена.")
                else:
                    print("Товар не найден.")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            name = input("Название товара: ")
            if current_store.remove_item(name):
                print("Товар удалён.")
            else:
                print("Товар не найден.")

        elif choice == "4":
            current_store.list_items()

        elif choice == "5":
            name = input("Название товара: ")
            price = current_store.get_price(name)
            if price is not None:
                print(f"Цена товара «{name}»: {price:.2f} руб.")
            else:
                print("Товар не найден.")

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

def run_manager_interface(store_manager: StoreManager):
    while True:
        print("\nМеню менеджера магазинов")
        print("1 - Показать список магазинов")
        print("2 - Выбрать магазин")
        print("3 - Найти самую низкую цену")
        print("0 - Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            store_manager.list_all_stores()

        elif choice == "2":
            store_manager.list_all_stores()
            name = input("Введите название магазина: ")
            selected_store = next((s for s in manager.stores if s.name == name), None)
            if selected_store:
                run_store_interface(selected_store)
            else:
                print("Магазин не найден.")

        elif choice == "3":
            query_item_name = input("Название товара: ")
            cheapest_offer = store_manager.find_cheapest(query_item_name)
            if cheapest_offer:
                cheapest_store_name, cheapest_price = cheapest_offer
                print(f"Самая низкая цена на '{query_item_name}' в магазине '{cheapest_store_name}': {cheapest_price:.2f} руб.")
            else:
                print("Товар не найден ни в одном магазине.")

        elif choice == "0":
            print("Выход из менеджера.")
            break

        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    run_manager_interface(manager)





