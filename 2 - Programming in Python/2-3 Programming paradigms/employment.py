class Employees:
    def __init__(self, name: str, last: str) -> None:
        self.name = name
        self.last = last


class Supervisors(Employees):
    def __init__(self, name: str, last: str, password: str) -> None:
        super().__init__(name, last)
        self.password = password


class Chefs(Employees):
    def __init__(self, name: str, last: str) -> None:
        super().__init__(name, last)

    def leave_request(self, days):
        return f"May I take leave for {days} days?"


adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.name)


class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True
