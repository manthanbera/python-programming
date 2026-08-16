class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, name):
        self.card_number = card_number
        self.name = name

    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card ({self.card_number[-4:]}) by {self.name}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Paid ₹{amount} using PayPal ({self.email})"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        return f"Paid ₹{amount} using Bitcoin (Wallet: {self.wallet_address[:8]}...)"


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)



processor = PaymentProcessor(CreditCardPayment("1234567890123456", "Manthan Bera"))
print(processor.process_payment(1500))

processor.set_strategy(PayPalPayment("manthanbera@gmail.com"))
print(processor.process_payment(2500))

processor.set_strategy(BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"))
print(processor.process_payment(50000))
