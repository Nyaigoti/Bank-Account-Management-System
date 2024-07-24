from bank_accounts import *

Goaty = bankAccount("Goaty", 1000)
Collo = bankAccount("Collo", 2000)

Goaty.getBalance()

Goaty.deposit(1000)

Goaty.withdraw(1000)

Goaty.transaction(500, Collo)