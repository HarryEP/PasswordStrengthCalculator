def user_input() -> str:
    password = input("Please input your password: ")
    return password


def calcuate_strength(password: str) -> int:
    for digit in password:
        print(digit)


def main():
    password = user_input()
    calcuate_strength(password)


if __name__ == "__main__":
    main()
