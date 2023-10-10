#!/usr/bin/env python3
# Created By: Tony Tran
# Date: Oct. 10, 2023
# This is program will calculate your hst and total using subtotal for Prince Edward Island.


import constants


def main():
    print("Prince Edward Island Tax Calculator")
    subtotal = float(input("Subtotal: "))
    HST = round(constants.HST * subtotal, 2)
    total = round(HST + subtotal, 2)
    print(f"HST: ${HST}\nTotal: ${total}")


if __name__ == "__main__":
    main()
