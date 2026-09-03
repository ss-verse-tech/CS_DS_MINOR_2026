# run time polymorphism

class Payment:
    def __init__(self, name, payment):
        self.name = name
        self.payment = payment

    def transaction(self):
        return "Transaction is done"


class UPI(Payment):
    def transaction(self):
        return f"Transaction is done by rs {self.payment-5}"

class Credit_Card(Payment):
    def transaction(self):
        return f"Transaction is done by rs {self.payment+5}"


c = Credit_Card("Rahul", 5000)
print(c.transaction())

    