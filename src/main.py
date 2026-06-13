import datetime
from utils import add, subtract

def main():
    name = "Jubaer Nur Mohammad"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    print(f"My name is {name}")
    print(f"Today's date is {today}")

def calculator_demo():
    print("\nCalculator Demo:")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")

if __name__ == "__main__":
    main()
    calculator_demo()