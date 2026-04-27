def total_salary(path):
    try:
        with open(path, encoding="utf-8") as file:
            salaries = []

            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 2:
                    raise ValueError(
                    f"Рядок {line_number}: очікується формат 'Ім'я,Зарплата', "
                    f"отримано: '{line}'"
                    )

                name, salary_str = parts
                name = name.strip()
                salary_str = salary_str.strip()

                if not name:
                    raise ValueError(
                        f"Рядок {line_number}: ім'я розробника порожнє."
                    )

                try:
                    salary = float(salary_str)

                except ValueError:
                    raise ValueError(
                        f"Рядок {line_number}: некоректне значення зарплати '{salary_str}'."
                    )


                if salary < 0 :
                    raise ValueError(
                        f"Рядок {line_number}: зарплата не може бути від'ємною ({salary})."
                    )

                salaries.append(salary)

            if not salaries:
                return 0, 0

            total = sum(salaries)
            average = total / len(salaries)
            return total, average

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Файл не знайдено: '{path}'"
        )

if __name__ == "__main__":
    total_sum, salary_avg = total_salary("ad1.txt")
    print(
        f"Загальна сума заробітної плати: {total_sum:.0f}, "
        f"Середня заробітна плата: {salary_avg:.0f}"
    )