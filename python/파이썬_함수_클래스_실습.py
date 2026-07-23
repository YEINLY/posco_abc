"""파이썬 함수와 클래스 기초 실습."""


def greet(name, message="안녕하세요"):
    """이름과 인사말을 받아 인사 문장을 반환합니다."""
    return f"{message}, {name}님!"


def calculate_average(numbers):
    """숫자 목록의 평균을 계산합니다."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def is_even(number):
    """숫자가 짝수인지 확인합니다."""
    return number % 2 == 0


class Student:
    """학생 이름과 점수를 관리하는 클래스입니다."""

    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        """학생의 평균 점수를 반환합니다."""
        return calculate_average(self.scores)

    def grade(self):
        """평균 점수를 기준으로 등급을 반환합니다."""
        average_score = self.average()
        if average_score >= 90:
            return "A"
        if average_score >= 80:
            return "B"
        if average_score >= 70:
            return "C"
        if average_score >= 60:
            return "D"
        return "F"

    def introduce(self):
        """학생 정보를 문장으로 반환합니다."""
        return f"{self.name}: 평균 {self.average():.1f}점, 등급 {self.grade()}"


class BankAccount:
    """입금과 출금을 연습하는 간단한 계좌 클래스입니다."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """금액을 입금하고 변경된 잔액을 반환합니다."""
        if amount <= 0:
            raise ValueError("입금액은 0보다 커야 합니다.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """금액을 출금하고 변경된 잔액을 반환합니다."""
        if amount <= 0:
            raise ValueError("출금액은 0보다 커야 합니다.")
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        self.balance -= amount
        return self.balance

    def summary(self):
        """계좌 정보를 문장으로 반환합니다."""
        return f"{self.owner}님의 잔액: {self.balance:,}원"


if __name__ == "__main__":
    print(greet("파이썬 학습자"))
    print(greet("홍길동", "반갑습니다"))
    print(f"평균: {calculate_average([80, 90, 70]):.1f}")
    print(f"8은 짝수인가요? {is_even(8)}")

    student = Student("홍길동", [85, 92, 78])
    print(student.introduce())

    account = BankAccount("홍길동", 10000)
    account.deposit(5000)
    account.withdraw(3000)
    print(account.summary())
