#Dia 21
import math
from collections import Counter

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return round(self.sum() / self.count())

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        counter = Counter(self.data)
        mode_value = counter.most_common(1)[0]
        return (mode_value[0], mode_value[1])

    def var(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return round(variance, 1)

    def std(self):
        return round(math.sqrt(self.var()), 1)

    def percentile(self, p):
        sorted_data = sorted(self.data)
        index = (p / 100) * (self.count() - 1)
        return sorted_data[int(index)]

    def freq_dist(self):
        counter = Counter(self.data)
        total = self.count()
        freq_list = []

        for value, count in counter.items():
            percentage = (count / total) * 100
            freq_list.append((round(percentage, 1), value))

        # sort descending by percentage
        freq_list.sort(reverse=True)
        return freq_list

    def describe(self):
        print("Count:", self.count())
        print("Sum: ", self.sum())
        print("Min: ", self.min())
        print("Max: ", self.max())
        print("Range: ", self.range())
        print("Mean: ", self.mean())
        print("Median: ", self.median())
        print("Mode: ", self.mode())
        print("Variance: ", self.var())
        print("Standard Deviation: ", self.std())
        print("Frequency Distribution:", self.freq_dist())




#DIA 21 PARTE 2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}    
        self.expenses = {}    

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Account Holder: {self.firstname} {self.lastname}")
        print("Total Income:", self.total_income())
        print("Total Expense:", self.total_expense())
        print("Account Balance:", self.account_balance())