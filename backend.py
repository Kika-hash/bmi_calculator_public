import random

from communication_base import *

bmi_ranges = {
    "underweight": 18.5,
    "normal_weight": 24.9,
    "over_weight": 29.9,
    "moderate_obesity": 34.9,
    "severe_obesity": 39.9,
}


def bmi_calculator(weight, height):
    bmi_value = weight / (height / 100) ** 2
    bmi_result = bmi_status(bmi_value, bmi_ranges)
    return bmi_result

def bmi_status(bmi_value, bmi_ranges):
    for key, value in bmi_ranges.items():
        if value > bmi_value:
            return key
    return "morbid_obesity"


def bmi_communication(bmi_status, underweight_mapping, normal_weight_mapping, over_weight_mapping):
    match bmi_status:
        case "underweight":
            return underweight_mapping
        case "normal_weight":
            return normal_weight_mapping
        case "over_weight":
            return over_weight_mapping
        case "moderate_obesity":
            return moderate_obesity_mapping
        case "severe_obesity":
            return severe_obesity_mapping
        case "morbid_obesity":
            return morbid_obesity_mapping

def rest_handler(weight, height):
    bmi = bmi_calculator(weight, height)
    communication = bmi_communication(bmi, underweight_mapping, normal_weight_mapping, over_weight_mapping)
    result = random.choice(communication)
    return result


def needle_calculation(weight, height):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5:
        response = 60
    elif bmi < 24.9:
        response = 90
    elif bmi < 29.9:
        response = 120
    elif bmi < 34.9:
        response = 180
    elif bmi < 39.9:
        response = 260
    else:
        response = 330

    return response

"""
while True:
    weight = int(input("Jaka jest twoja waga (kg)?\n"))
    height = int(input("Jaki jest twój wzrost (cm)?\n"))
    bmi = bmi_calculator(weight, height)
    communication = bmi_communication(bmi, underweight_mapping, normal_weight_mapping, over_weight_mapping)
    result = random.choice(communication)
    print(result + "\n")

"""

