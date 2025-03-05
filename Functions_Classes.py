# def sum_even(num):
#     if num%2==1:
#         num -= 1
#     sum=0
#     while num > 0:
#         sum += num
#         num -= 2
#     return sum
# print(sum_even(7))

# def Calculate_BMI(Weight, Height):
#     return (Weight / (Height * Height))
# print(Calculate_BMI(14,18))

# def count_down_up(n):
#     for i in range (n, 1, -1):
#         print(i)
#     for i in range (1, n+1, +1):
#         print(i)
# count_down_up(6)

class BankAccount:
    def __init__(self, Name, Account_Number, Initial_Balance):
        self.Name = Name
        self.Account_Number = Account_Number
        self.Balance = Initial_Balance
    def Deposit(self, Amount):
        self.Balance += Amount
    def Withdraw(self, Amount):
        if Amount > self.Balance:
            print("Not enought money in balance.")
        else: self.Balance -= Amount
    def Check_Balance(self):
        print(self.Balance)
Gary = BankAccount("Gary", 12, 1020)
Gary.Check_Balance()
Gary.Deposit(400)
Gary.Check_Balance()
Gary.Withdraw(2000)
Gary.Withdraw(700)
Gary.Check_Balance()
