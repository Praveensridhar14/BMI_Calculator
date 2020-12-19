import json


def BMI_Caculator(heightCM, WeightKg):
    height_in_sq_metre = heightCM/ 100
    bmi_value = round(WeightKg / height_in_sq_metre  ** 2, 2)
    return bmi_value


def main():
    with open("user_data.json", "r") as fptr:
            user_details = json.load(fptr)
    over_weight_people = 0
    user_data_with_bmi = []
    for user_data in user_details:
        bmi_value = BMI_Caculator(user_data["HeightCm"], user_data["WeightKg"] )
        user_data["BMI_Value"] = bmi_value
        user_data_with_bmi.append(user_data)
        if bmi_value > 25:
            over_weight_people += 1
    print("The number of over weight people is %d" %over_weight_people)
    with open("user_data_with_bmi.json", "w") as fptr:
        json.dump(user_data_with_bmi,fptr, indent = 4)



if __name__ == '__main__':
    main()