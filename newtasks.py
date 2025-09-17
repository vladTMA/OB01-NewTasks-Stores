from datetime import date, datetime

class Task:
    def __init__ (self, description: str, deadline: date, status: bool = False):
        self.description = description
        self.deadline = deadline
        self.status = status # False = не выполнено, True = выполнено

    def is_pending(self) -> bool:
        """Проверить, находится ли задача на исполнении"""
        return not self.status

    def mark_done(self) -> None:
        """Отметить задачу как выполненную"""
        self.status = True

    def is_overdue(self) -> bool:
        """Проверить, просрочена ли задача"""
        return not self.status and self.deadline < date.today()

    def show(self) -> None:
        formatted_date = f"{self.deadline.day}.{self.deadline.month}.{self.deadline.year}"
        status_text = "✅ Выполнено" if self.status else (
            "⚠️ Просрочена" if self.is_overdue() else "🕒 На исполнении"
        )
        print(f"Задача: {self.description}\n📅 Срок: {formatted_date}\n Статус: {status_text}")

def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, "%d.%m.%Y").date()

task1 = Task("Сделать отчёт", parse_date("16.9.2025"))
task2 = Task("Позвонить клиенту", parse_date("17.9.2025"))
task3 = Task("Отправить презентацию", parse_date("10.10.2025"), status=True)

task1.show()
task2.show()
task3.show()






