# ------------------------------------------------------------
# CS 3200 Project: Food Insecurity Database Program
# By: Jorge Barron, Yuezhu (Sarah) Lang, Alvin Kannalath
# ------------------------------------------------------------

# importing the necessary libraries for the project
import pymysql

print("--------------------------------------------------------------------------------------------")
print("Welcome to the Food Insecurity Database program. Please enter the following information to continue:")
print("--------------------------------------------------------------------------------------------")

# prompting user to provide their MYSQL username and password
check = True
while check:
    try:
        mysql_username = str(input("What is your MySQL username? "))
        mysql_password = str(input("What is your MySQL password? "))

        # connecting python to MySQL with the MySQL username and password provided by the user
        # (if it cannot connect for any given reason, this will throw an error)
        cnx = pymysql.connect(host='localhost', user=mysql_username, password=mysql_password,
                          db='food_insecurity', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        # notifying the user that they connected to SharkDB successfully
        print("Successfully connected to the 'Food Insecurity' database.\n")
        check = False
    except Exception as e:
        print('Wrong username and password. Please try again')
        print()
        check = True

def user_consult_tables() :
    print("\n You have chosen to consult the possible values in the table in the current database.")
    print("--------------------------------------------------------------------------------------------")
    print("Here are the possible values you can choose for areas/countries: \n")
    cur_show_user_area_options = cnx.cursor()
    stmt_user_area_options = "select * from area"

    cur_show_user_area_options.execute(stmt_user_area_options)

    user_area_options_output = cur_show_user_area_options.fetchall()

    for row in user_area_options_output :
        print(row)

    print("--------------------------------------------------------------------------------------------")
    print("Here are the possible items you may choose: \n")
    cur_show_user_item_options = cnx.cursor()
    stmt_user_item_options = "select item_code, item, element_code from item_table"

    cur_show_user_item_options.execute(stmt_user_item_options)

    user_item_options_output = cur_show_user_item_options.fetchall()

    for row in user_item_options_output :
        print(row)

    print("--------------------------------------------------------------------------------------------")
    print("Here are the possible units you may choose: \n")
    cur_show_user_unit_options = cnx.cursor()
    stmt_user_unit_options = "select * from unit_table"

    cur_show_user_unit_options.execute(stmt_user_unit_options)

    user_unit_options_output = cur_show_user_unit_options.fetchall()

    for row in user_unit_options_output :
        print(row)

    print("--------------------------------------------------------------------------------------------")
    print("Here are the possible years you may choose: \n")
    cur_show_user_year_options = cnx.cursor()
    stmt_user_year_options = "select * from year"

    cur_show_user_year_options.execute(stmt_user_year_options)

    user_year_options_output = cur_show_user_year_options.fetchall()

    for row in user_year_options_output :
        print(row)

    print("--------------------------------------------------------------------------------------------")

    main()


# function for the create operations the user can do
def user_add_values():
    print("--------------------------------------------------------------------------------------------")
    print("You can now create new tuples in the database, please provide the following information: \n")
    print("A. Add an entire new tuple to the database including all values for all tables")
    print("B. Create & View the total number of values in the country")
    print("--------------------------------------------------------------------------------------------")
    user_add_value_choice = str(input("Provide your option as a letter: "))

    if user_add_value_choice == "A" :
        print("\n You can now add an entire new tuple to the database. Please provide the following data: \n")

        cur_add_value = cnx.cursor()

        check = True
        while check:
            try:
                user_add_value_new_year_code = int(input("Enter the new year code: "))
                check = False
            except ValueError:
                print("Invalid inputs. Please try again!")

        user_add_value_new_year = str(input("Enter the new year: "))

        check = True
        while check:
            try:
                user_add_value_new_item_code = int(input("Enter the new item code: "))
                check = False
            except ValueError:
                print("Invalid inputs. Please try again!")

        user_add_value_new_item = str(input("Enter the new item: "))

        check = True
        while check:
            try:
                user_add_value_new_element_code = int(input("Enter the new element code: "))
                check = False
            except ValueError:
                print("Invalid inputs. Please try again!")

        check = True
        while check:
            try:
                user_add_value_new_area_code = int(input("Enter the new area code: "))
                check = False
            except ValueError:
                print("Invalid inputs. Please try again!")

        user_add_value_new_area = str(input("Enter the new area: "))
        user_add_value_new_unit = str(input("Enter the new unit: "))

        check = True
        while check:
            try:
                user_add_value_new_value = int(input("Enter the new value: "))
                check = False
            except ValueError:
                print("Invalid inputs. Please try again!")


        stmt_create_value_procedure = "call createValue(" + str(
            user_add_value_new_year_code) + "," + "'" + user_add_value_new_year + "'" + "," + str(
            user_add_value_new_item_code) + "," + "'" + user_add_value_new_item + "'" + "," + str(
            user_add_value_new_element_code) + "," + str(
            user_add_value_new_area_code) + "," + "'" + user_add_value_new_area + "'" + "," + "'" + user_add_value_new_unit + "'" + "," + str(
            user_add_value_new_value) + ")"

        try:
            cur_add_value.execute(stmt_create_value_procedure)
            print(
                "\n Successfully created new tuple in database. Please query the data using option #2 to see the new data added.")
            cnx.commit()
        except pymysql.err.IntegrityError:
            print("You have entered values that do not match. Item code must match item and element code. Year code must match year. Element code must match unit. Area code must match area")

    elif user_add_value_choice == "B" :
        print("\n You are now creating and finding the number of values in the country of your choice.\n")

        cur_add_value_column = cnx.cursor()

        check = True
        while check:
            try:
                user_country_code_choice = int(input("Please enter the area code of the country: "))
                check = False
            except ValueError:
                print("Invalid input. Please try again. Number needed!")

        try:
            stmt_initialize_value_per_country = "CALL initialize_value_per_country" + "(" + str(user_country_code_choice) + ")"
            stmt_get_value_per_country = "SELECT value_per_country FROM area WHERE area_code = " + str(user_country_code_choice) + ";"
            cur_add_value_column.execute(stmt_initialize_value_per_country)
            cur_add_value_column.execute(stmt_get_value_per_country)
            user_view_value_per_country = cur_add_value_column.fetchall()
            value_per_country_count = user_view_value_per_country[0]['value_per_country']

            print("There are " + str(value_per_country_count) + " values in country with area_code " + str(user_country_code_choice))
            print("Successfully created new value.")
        except IndexError:
            print("Please try again. This area code was not found")
            user_add_values()

    else :
        print("\n ERROR: Invalid choice, please re-input: ")
        user_add_values()

    main()


# function for the read operations the user can do
def user_view_values():
    print("--------------------------------------------------------------------------------------------")
    print("You will now view tuples, please enter which option you would like to query: \n")
    print("A. Find a value with year, item, and area code")
    print("B. Find the area code for a given country")
    print("C. Find the maximum value and year for a given area and item code")
    print("D. Find the smallest value and year for a given area and item code")
    print("E. Find the smallest value and country for a given year and item code ")
    print("F. Find the maximum value and country for a given year and item code")
    print("G. Find the maximum value along with its country and year for a given item code")
    print("H. Find the minimum value along with its country and year for a given item code")
    print("--------------------------------------------------------------------------------------------")

    user_choose_view_value = input("Choose which option you choose:")

    if user_choose_view_value == "A" :
        print(" \n You can now find a value with a given year, item and area code. Provide the following input: \n")

        cur_view_find_value = cnx.cursor()

        check = True
        while check:
            try:
                user_year_code = int(input("Enter the year code: "))
                user_item_code = int(input("Enter the item code: "))
                user_area_code = int(input("Enter the area code: "))
                check = False
            except ValueError:
                print("Please re-enter in valid inputs! (Numbers)")
                check = True


        stmt_view_value = "CALL findValue(" + str(user_year_code) + "," + str(user_item_code) + "," + str(
            user_area_code) + ")"

        cur_view_find_value.execute(stmt_view_value)

        user_view_values_output = cur_view_find_value.fetchall()

        print("\n Selected value is " + str(user_view_values_output))

    elif user_choose_view_value == "B" :
        print("\n You can now find the area code for a given country. Provide the following input: \n ")

        cur_view_find_country_id = cnx.cursor()

        user_country_code_find_country_id = input("Enter your desired country: ")

        stmt_find_country_id_func = "SELECT findCountryID('" + user_country_code_find_country_id + "')"

        cur_view_find_country_id.execute(stmt_find_country_id_func)

        user_find_country_id_output = cur_view_find_country_id.fetchall()

        print("\n The country ID for your country is " + str(user_find_country_id_output))


    elif user_choose_view_value == "C" :
        print("\n You can now find the maximum value and year for a given area and item code. Provide the following input: \n")
        cur_view_most_val_year_for_area = cnx.cursor()

        check = True
        while check:
            try:
                user_view_most_val_year_for_area_area_code = int(input("Enter the area code: "))
                user_view_most_val_year_for_area_item_code = int(input("Enter the item code: "))
                check = False
            except ValueError:
                print("Please re-enter valid inputs (Numbers)!")
                check = True

        stmt_most_val_year_for_area = "CALL most_val_year_for_area(" + str(user_view_most_val_year_for_area_area_code) + "," + str(user_view_most_val_year_for_area_item_code) + ")"

        cur_view_most_val_year_for_area.execute(stmt_most_val_year_for_area)

        user_most_val_year_for_area_output = cur_view_most_val_year_for_area.fetchall()

        print("\n The maximum value and year for your inputs are: " + str(user_most_val_year_for_area_output))


    elif user_choose_view_value == "D" :
        print("\n You can now find the smallest value and year for a given area and item code. Provide the following input: \n")

        cur_view_least_val_year_for_area = cnx.cursor()

        check = True
        while check:
            try:
                user_view_least_val_year_for_area_area_code = int(input("Enter the area code: "))
                user_view_least_val_year_for_area_item_code = int(input("Enter the item code: "))
                check = False
            except ValueError:
                print("Please re-enter valid inputs (Numbers)!")
                check = True

        stmt_least_val_year_for_area = "CALL least_val_year_for_area(" + str(user_view_least_val_year_for_area_area_code) + "," + str(user_view_least_val_year_for_area_item_code) + ")"

        cur_view_least_val_year_for_area.execute(stmt_least_val_year_for_area)

        user_least_val_year_for_area_output = cur_view_least_val_year_for_area.fetchall()

        print("\n The minimum value and year for your inputs are: " + str(user_least_val_year_for_area_output))


    elif user_choose_view_value == "E" :
        print("\n You can now find the smallest value and country for a given year and item code. Provide the following input: \n")

        cur_view_least_val_area_for_year = cnx.cursor()

        check = True
        while check:
            try:
                user_view_least_val_area_for_year_code = int(input("Enter the year code: "))
                user_view_least_val_area_for_year_item_code = int(input("Enter the item code: "))
                check = False
            except ValueError:
                print("Please re-enter valid inputs (Numbers)!")
                check = True

        stmt_least_val_area_for_year = "CALL least_val_area_for_year(" + str(user_view_least_val_area_for_year_code) + "," + str(user_view_least_val_area_for_year_item_code) + ")"

        cur_view_least_val_area_for_year.execute(stmt_least_val_area_for_year)

        user_least_val_area_for_year_output = cur_view_least_val_area_for_year.fetchall()

        print("\n The smallest value and country for your inputs are: " + str(user_least_val_area_for_year_output))

    elif user_choose_view_value == "F" :
        print("\n You can now find the maximum value and country for a given year and item code. Provide the following input: \n")

        cur_view_most_val_area_for_year = cnx.cursor()

        check = True
        while check:
            try:
                user_view_most_val_area_for_year_code = int(input("Enter the year code: "))
                user_view_most_val_area_for_year_item_code = int(input("Enter the item code: "))
                check = False
            except ValueError:
                print("Please re-enter valid inputs (Numbers)!")
                check = True

        stmt_most_val_area_for_year = "CALL most_val_area_for_year(" + str(
            user_view_most_val_area_for_year_code) + "," + str(user_view_most_val_area_for_year_item_code) + ")"

        cur_view_most_val_area_for_year.execute(stmt_most_val_area_for_year)

        user_most_val_area_for_year_output = cur_view_most_val_area_for_year.fetchall()

        print("\n The maximum value and country for your inputs are: " + str(user_most_val_area_for_year_output))


    elif user_choose_view_value == "G" :
        print("\n You can now find the maximum value, country, and year, for a given item code. Provide the following input: \n")

        cur_overall_max = cnx.cursor()

        check = True
        while check:
            try:
                user_overall_max_item_code = int(input("Enter the item code: "))
                check = False
            except ValueError:
                print("Please re-enter valid inputs (Numbers)!")
                check = True

        stmt_overall_max_procedure = "CALL overall_max(" + str(user_overall_max_item_code) + ")"

        cur_overall_max.execute(stmt_overall_max_procedure)

        user_overall_max_output = cur_overall_max.fetchall()

        print("\n The maximum value, country, and year for your inputs are: " + str(user_overall_max_output))


    elif user_choose_view_value == "H" :
        print("\n You can now find the minimum value, country, and year, for a given item code. Provide the following input:  \n")
        cur_overall_min = cnx.cursor()

        check = True
        while check:
            try:
                user_overall_min_item_code = int(input("Enter the item code: "))
                check = False
            except ValueError:
                print("Please re-enter valid inputs (Numbers)!")
                check = True


        stmt_overall_min_procedure = "CALL overall_min(" + str(user_overall_min_item_code) + ")"

        cur_overall_min.execute(stmt_overall_min_procedure)

        user_overall_min_output = cur_overall_min.fetchall()

        print("\n The minimum value, country, and year for your inputs are: " + str(user_overall_min_output))
    else :
        print("\n ERROR: Invalid choice, please re-input: ")
        user_view_values()

    main()


# function for the user delete operation
def user_delete_values():
    print("--------------------------------------------------------------------------------------------")
    print("\n You can now delete tuples in the database, please provide the following information to proceed: ")
    print("--------------------------------------------------------------------------------------------")

    cur_delete_value = cnx.cursor()

    user_update_value_area_code = int(input("Enter the area code: "))
    user_update_value_year_code = int(input("Enter the year code: "))
    user_update_value_item_code = int(input("Enter the item code: "))

    stmt_delete_value = "delete from value_table where area_code =" + str(
        user_update_value_area_code) + " and year_code = " + str(
        user_update_value_year_code) + " and item_code = " + str(user_update_value_item_code)

    cur_delete_value.execute(stmt_delete_value)
    print("\n Successfully deleted tuple from the value_table in the database.")

    cnx.commit()

    main()


# function for the user update operation
def user_update_values():
    print("--------------------------------------------------------------------------------------------")
    print("\n You can now update tuples in the database, please provide which information you want to update: ")
    print("--------------------------------------------------------------------------------------------")

    cur_update_value = cnx.cursor()

    check = True
    while check:
        try:
            user_update_value_year_code = int(input("Enter the year code: "))
            check = False
        except ValueError:
            print("Invalid input. You need to enter a valid year code")
            check = True

    check = True
    while check:
        try:
            user_update_value_item_code = int(input("Enter the item code: "))
            check = False
        except ValueError:
            print("Invalid input. You need to enter a valid item code")
            check = True

    check = True
    while check:
        try:
            user_update_value_area_code = int(input("Enter the area code: "))
            check = False
        except ValueError:
            print("Invalid input. You need to enter a valid area code")
            check = True

    check = True
    while check:
        try:
            user_update_value_input = int(input("Enter the new value to update: "))
            check = False
        except ValueError:
            print("Invalid input. You need to enter a valid value (number)")
            check = True

    stmt_create_value_procedure = "call updateValue(" + str(user_update_value_year_code) + "," + str(
        user_update_value_item_code) + "," + str(user_update_value_area_code) + "," + str(user_update_value_input) + ")"

    cur_update_value.execute(stmt_create_value_procedure)

    print("\n Successfully updated tuple with value " + str(user_update_value_input) + " in database.")

    cnx.commit()

    main()


# option for ending the whole application
def end_application_program():
    print("--------------------------------------------------------------------------------------------")
    print("\n You have successfully quit the Food Insecurity database program.")
    print("\n The connection has closed to the database.")
    print("--------------------------------------------------------------------------------------------")
    cnx.close()


def main():

    print("--------------------------------------------------------------------------------------------")
    print(
        "Welcome to the Food Insecurity Database Application, please enter the number according to the feature you want to utilize:")
    print("0. Consult the existing values in the database")
    print("1. Create new values in the database")
    print("2. Read values in the database")
    print("3. Delete values in the database")
    print("4. Update values in the database")
    print("5. END the application program.")
    print("--------------------------------------------------------------------------------------------")

    try:
        user_choice = int(input("Enter your choice as a number: "))

    except ValueError:
        print("Please enter a valid number!")
        main()

    if (user_choice == 0) :
        user_consult_tables()
    elif (user_choice == 1):
        user_add_values()
    elif (user_choice == 2):
        user_view_values()
    elif (user_choice == 3):
        user_delete_values()
    elif (user_choice == 4):
        user_update_values()
    elif (user_choice == 5):
        end_application_program()
    else :
        print("\n Invalid input, please enter one of the options: \n")
        main()

if __name__ == '__main__':
    main()
