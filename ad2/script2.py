def get_cats_info(path):
    try:
        with open(path, encoding="utf-8") as file:
            cats = []

            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 3:
                    raise ValueError(
                        f"Рядок {line_number}: очікується формат 'id,ім'я,вік', "
                        f"отримано: '{line}'"
                    )

                cat_id, name, age = parts

                if not cat_id.strip():
                    raise ValueError(
                        f"Рядок {line_number}: id кота порожній."
                    )

                if not name.strip():
                    raise ValueError(
                        f"Рядок {line_number}: ім'я кота порожнє."
                    )

                if not age.strip().isdigit():
                    raise ValueError(
                        f"Рядок {line_number}: вік має бути цілим числом, "
                        f"отримано: '{age.strip()}'"
                    )

                cats.append({
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip(),
                })

            return cats

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Файл не знайдено: '{path}'"
        )

if __name__ == "__main__":
    cats_info = get_cats_info("ad2.txt")
    for cat in cats_info:
        print(cat)