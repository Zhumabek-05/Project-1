import datetime
import os
from abc import ABC, abstractmethod

# --- ТАПСЫРМА 1: DEVICE АБСТРАКЦИЯСЫ ---
class Device(ABC):
    @abstractmethod
    def operate(self):
        pass

    @abstractmethod
    def power_source(self):
        pass


class Phone(Device):
    def operate(self):
        return "-> Phone: Қоңырау шалып, интернетке қосылады."

    def power_source(self):
        return "-> Phone: Батареяны пайдаланады."


class Tablet(Device):
    def operate(self):
        return "-> Tablet: Оқу және ойын үшін қолданылады."

    def power_source(self):
        return "-> Tablet: Батарея арқылы жұмыс істейді."


def run_task1():
    print("--- ТАПСЫРМА 1: DEVICE АБСТРАКЦИЯСЫ ---")
    my_phone = Phone()
    my_tablet = Tablet()

    print(f"\n[Phone]: {my_phone.operate()}")
    print(f"[Phone]: {my_phone.power_source()}")

    print(f"\n[Tablet]: {my_tablet.operate()}")
    print(f"[Tablet]: {my_tablet.power_source()}")
    print("-" * 50)


# --- ТАПСЫРМА 2: STORAGE ИНТЕРФЕЙСІ ---
class StorageInterface(ABC):
    @abstractmethod
    def connect(self): pass

    @abstractmethod
    def disconnect(self): pass

    @abstractmethod
    def execute(self, query): pass


class LocalStorage(StorageInterface):
    def connect(self):
        print("-> LocalStorage: Дискке қосылу орнатылды.")

    def disconnect(self):
        print("-> LocalStorage: Қосылым ажыратылды.")

    def execute(self, query):
        print(f"-> LocalStorage: Файл операциясы орындалды: '{query}'")


class CloudStorage(StorageInterface):
    def connect(self):
        print("-> CloudStorage: Интернет арқылы қосылу орнатылды.")

    def disconnect(self):
        print("-> CloudStorage: Қосылым жабылды.")

    def execute(self, query):
        print(f"-> CloudStorage: Сұрау орындалды: '{query}'")


def run_task2():
    print("--- ТАПСЫРМА 2: STORAGE ИНТЕРФЕЙСІ ---")
    local = LocalStorage()

    local.connect()
    local.execute("READ users.json")
    local.disconnect()

    print("-" * 50)


# --- ТАПСЫРМА 3: NOTIFIER ---
class Notifier(ABC):
    def format_message(self, message: str) -> str:
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        return f"{timestamp} - {message}"

    @abstractmethod
    def notify(self, message: str):
        pass


class ScreenNotifier(Notifier):
    def notify(self, message: str):
        formatted_msg = self.format_message(f"[SCREEN] {message}")
        print(f"Экран: {formatted_msg}")


class FileNotifier(Notifier):
    def __init__(self, filename="system_log.txt"):
        self.filename = filename
        if os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write("")

    def notify(self, message: str):
        formatted_msg = self.format_message(f"[FILE] {message}")
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(formatted_msg + "\n")
        print(f"Файлға жазылды: {message}")


def run_task3():
    print("--- ТАПСЫРМА 3: NOTIFIER ---")
    screen = ScreenNotifier()
    file = FileNotifier()

    screen.notify("Жүйе іске қосылды.")
    file.notify("Қате анықталды: 404.")

    print(f"\n[{file.filename} файлының мазмұны]:")
    try:
        with open(file.filename, 'r', encoding='utf-8') as f:
            print(f.read().strip())
    except FileNotFoundError:
        pass
    print("-" * 50)


# --- ТАПСЫРМА 4: ПОЛИМОРФИЗМ ---
class Laptop(Device):
    def operate(self): return "-> Laptop: Жұмыс және бағдарламалау үшін қолданылады."
    def power_source(self): return "-> Laptop: Батарея немесе электр қуаты."


class SmartWatch(Device):
    def operate(self): return "-> SmartWatch: Уақытты көрсетіп, денсаулықты бақылайды."
    def power_source(self): return "-> SmartWatch: Батареяны пайдаланады."


def run_task4():
    print("--- ТАПСЫРМА 4: ПОЛИМОРФИЗМ ---")
    device_list = [Phone(), Tablet(), Laptop(), SmartWatch()]

    for device in device_list:
        print(f"{device.__class__.__name__}: {device.operate()}")

    print("-" * 50)


# --- ТАПСЫРМА 5: DELIVERY SYSTEM ---
class DeliverySystem(ABC):
    @abstractmethod
    def authorize(self, amount): pass

    @abstractmethod
    def process(self, amount): pass

    @abstractmethod
    def refund(self, transaction_id): pass


class DHL(DeliverySystem):
    def authorize(self, amount):
        print(f"-> DHL: {amount} KZT үшін жеткізу авторизациясы сұралды.")

    def process(self, amount):
        print(f"-> DHL: {amount} KZT жеткізу төлемі өңделді.")

    def refund(self, transaction_id):
        print(f"-> DHL: Транзакция ID {transaction_id} бойынша қайтару жүргізілді.")


class FoodExpress(DeliverySystem):
    def authorize(self, amount):
        print(f"-> FoodExpress: {amount} KZT үшін жеткізу авторизациясы.")

    def process(self, amount):
        print(f"-> FoodExpress: {amount} KZT жеткізу төлемі өңделді.")

    def refund(self, transaction_id):
        print(f"-> FoodExpress: Транзакция ID {transaction_id} бойынша қайтару қабылданды.")


def run_task5():
    print("--- ТАПСЫРМА 5: DELIVERY SYSTEM ---")

    dhl = DHL()
    food = FoodExpress()

    amount = 5500
    txn_id = "TXN_987654"

    print("\n[DHL әрекеттері]:")
    dhl.authorize(amount)
    dhl.process(amount)
    dhl.refund(txn_id)

    print("\n[FoodExpress әрекеттері]:")
    food.authorize(amount)
    food.process(amount)
    food.refund(txn_id)

    print("-" * 50)


if __name__ == "__main__":
    run_task1()
    print("\n")
    run_task2()
    print("\n")
    run_task3()
    print("\n")
    run_task4()
    print("\n")
    run_task5()
