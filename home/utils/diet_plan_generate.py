from operator import ge
from re import T
from typing import Literal
import random

PROTEIN_LIST = [
    "Йогурт (1 чашка)",
    "Приготовленное мясо (100 г)",
    "Приготовленная рыба (130 г)",
    "1 целое яйцо + 4 белка",
    "Тофу (160 г)",
]

FRUIT_LIST = [
    "Ягоды (300 г)",
    "Яблоко",
    "Апельсин",
    "Банан",
    "Сушеные фрукты (горсть)",
    "Фруктовый сок (125 мл)",
]

VEGETABLE_LIST = [
    "Любые овощи (80г)",
]

GRAINS_LIST = [
    "Приготовленные злаки (150 г)",
    "Хлеб из цельного зерна (1 ломтек)",
    "Половина большого картофеля (75 г)",
    "Овсянка (250 г)",
    "2 кукурузных тортильи",
]
PS_LIST = [
    "Соя (25 г)",
    "Обезжиренное молоко (250 мл)",
    "Хумус (4 ст. ложки)",
    "Творог (125 г)",
    "Вкусный йогурт (125 г)",
]
TASTE_EN_LIST = [
    "2 ч. ложки (10 мл) оливкового масла",
    "2 ст. ложки (30 г) соуса для салата с пониженным содержанием калорий",
    "1/4 среднего авокадо",
    "Небольшой горсть орехов",
    "15 грамм тертого пармезана",
    "1 ст. ложка (20 г) варенья, желе, меда, сиропа, сахара",
]

ACTIVITIES = {
    "Сидячий (мало или отсутствует физическая активность)": 1.2,
    "Легкая активность (1-3 дня в неделю)": 1.375,
    "Умеренная активность (3-5 дней в неделю)": 1.55,
    "Очень активный (6-7 дней в неделю)": 1.725,
    "Супер активный (два раза в день)": 1.9,
}


def get_calories(
    gender: Literal["Мужчина", "Женщина"],
    weight: "int > 0",
    height: "int > 0",
    age: "int > 0",
    activity: str,
) -> int:
    match gender:
        case "Мужчина":
            cal = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
        case "Женщина":
            cal = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
        case _:
            raise ValueError("Wrong parameter gender")
    if activity not in ACTIVITIES:
        raise ValueError("Wrong parameter activity")
    return int(ACTIVITIES[activity] * cal)


def one_day_diet_plan(
    gender: Literal["Мужчина", "Женщина"],
    weight: "int > 0",
    height: "int > 0",
    age: "int > 0",
    activity: str,
) -> dict:
    result = dict()
    weight = float(weight) if weight else 0
    height = float(height) if height else 0
    age = float(age) if age else 0
    activity = str(activity)
    cal = get_calories(
        gender=gender,
        weight=weight,
        height=height,
        age=age,
        activity=activity,
    )
    result["cal"] = cal
    if cal < 1500:
        result["breakfast"] = (
            "Завтрак: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
        )
        result["lunch"] = (
            "Обед: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(PS_LIST)}"
        )

        result["afternoon_snack"] = (
            "Полдник: " f"{random.choice(PS_LIST)}" " + " f"{random.choice(FRUIT_LIST)}"
        )

        result["dinner"] = (
            "Ужин: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            "2"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(TASTE_EN_LIST)}"
        )

        result["evening_snack"] = "Вечерний перекус: " f"{random.choice(FRUIT_LIST)}"
    elif cal < 1800:
        result["breakfast"] = (
            "Завтрак: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
        )

        result["lunch"] = (
            "Обед: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(PS_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
        )

        result["afternoon_snack"] = (
            "Полдник: " f"{random.choice(PS_LIST)}" " + " f"{random.choice(FRUIT_LIST)}"
        )

        result["dinner"] = (
            "Ужин: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            "2"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(TASTE_EN_LIST)}"
        )

        result["evening_snack"] = "Вечерний перекус: " f"{random.choice(FRUIT_LIST)}"

    elif cal < 2200:
        result["breakfast"] = (
            "Завтрак: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
        )

        result["lunch"] = (
            "Обед: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(PS_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
        )

        result["afternoon_snack"] = (
            "Полдник: " f"{random.choice(PS_LIST)}" " + " f"{random.choice(FRUIT_LIST)}"
        )

        result["dinner"] = (
            "Ужин: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            "2"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(TASTE_EN_LIST)}"
        )

        result["evening_snack"] = "Вечерний перекус: " f"{random.choice(FRUIT_LIST)}"
    else:
        result["breakfast"] = (
            "Завтрак: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
            " + "
            f"{random.choice(GRAINS_LIST)}"
        )

        result["lunch"] = (
            "Обед: "
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            f"{random.choice(PS_LIST)}"
            " + "
            f"{random.choice(FRUIT_LIST)}"
        )

        result["afternoon_snack"] = (
            "Полдник: " f"{random.choice(PS_LIST)}" " + " f"{random.choice(FRUIT_LIST)}"
        )

        result["dinner"] = (
            "Ужин: 2"
            f"{random.choice(PROTEIN_LIST)}"
            " + "
            "2"
            " + "
            f"{random.choice(VEGETABLE_LIST)}"
            " + "
            "Листовая зелень"
            " + "
            f"{random.choice(GRAINS_LIST)}"
            " + "
            "2"
            " + "
            f"{random.choice(TASTE_EN_LIST)}"
        )

        result["evening_snack"] = "Вечерний перекус: " f"{random.choice(FRUIT_LIST)}"

    return result


def days_diet_plan(
    number_of_days: "int > 0",
    gender: Literal["Мужчина", "Женщина"],
    weight: "int > 0",
    height: "int > 0",
    age: "int > 0",
    activity: str,
) -> list[dict]:
    number_of_days = int(number_of_days) if number_of_days else 0
    result = []
    for _ in range(number_of_days):
        result.append(
            one_day_diet_plan(
                gender=gender,
                weight=weight,
                height=height,
                age=age,
                activity=activity,
            )
        )
    return result
