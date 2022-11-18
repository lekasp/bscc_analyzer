from data_grabber import grab_data, get_company


"""def is_woman(json_data):
    try:
        gender = json_data["personal_information"]["gender"]["inferred"]
    except Exception:
        return False

    if gender == "Female":
        return True
    return False"""


def count_companies():
    companie_names = {}

    data_list = grab_data()
    for data_point in data_list:
        name = get_company(data_point)

    print(companie_names)