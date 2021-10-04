def another_new_feature():
    """another new feature from second-homework-conflict branch"""
    pass


physical_quantities_and_units = {"pressure": {"pascal", "atmosphere", "mercury.column"}}
print("Welcome to currency converter!")
while True:
    print("Please, enter via space:\n\n"
          "the name of your physical quantity from the list,\n"
          "value of the physical quantity,\n"
          "initial metric unit,\n"
          "final metric unit\n\n"
          "quantities list (available metric units in brackets):\n\n"
          "pressure (pascal, atmosphere, mercury.column),\n"
          "temperature and weight will be available in future\n")
    parameters = input("Enter parameters: ").split()
    if (len(parameters)) == 4:
        quantity, value, in_unit, out_unit = parameters[0], parameters[1], parameters[2], parameters[3]
        if (quantity in physical_quantities_and_units and
                str.isdigit(value.replace("-", "").replace(".", "")) is True):
            if (in_unit in physical_quantities_and_units[parameters[0]] and
                    out_unit in physical_quantities_and_units[parameters[0]]):
                value = float(parameters[1])
                if quantity == "pressure":
                    if in_unit == "pascal" and out_unit == "atmosphere":
                        x = value / (0.980665 * 10 ** 5)
                        print(x, "atmosphere", sep=" ")
                    elif in_unit == "atmosphere" and out_unit == "pascal":
                        x = value * (0.980665 * 10 ** 5)
                        print(x, "pascal", sep=" ")
                    elif in_unit == "pascal" and out_unit == "mercury.column":
                        x = value / 133.3224
                        print(x, "mercury.column", sep=" ")
                    elif in_unit == "mercury.column" and out_unit == "pascal":
                        x = value * 133.3224
                        print(x, "pascal", sep=" ")
                    elif in_unit == "atmosphere" and out_unit == "mercury.column":
                        x = value * 760
                        print(x, "mercury.column", sep=" ")
                    elif in_unit == "mercury.column" and out_unit == "atmosphere":
                        x = value / 760
                        print(x, "atmosphere", sep=" ")
            else:
                print("Your initial or final metric unit is not from the list. Please, reenter parameters\n")
                continue
        else:
            print(
                "Your quantity is not from the list or your value does not match format. Please, reenter parameters\n")
            continue
    else:
        print(
            "You have entered wrong number of parameters. There are 4 parameters required. Please, reenter "
            "parameters\n")
        continue
