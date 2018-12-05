
def strings(s):
    str = {
        "no_money": "Not enough money to buy.",
        "err_pc": "Enter a number between 2-4 please."
    }
    return str.get(s)
