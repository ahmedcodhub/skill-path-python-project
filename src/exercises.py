"""In this file, you will find the exercises to complete.

If you cannot complete an exercise, and you need the result for following exercises, then we have included a commented
out import statement like this: `# from .solutions.exercise_1_1 import order_strings`. This was created with only a
very limited set of data and is no replacement for your own solution in order to successfully complete these exercises.
If you need help, please consult your mentor.

Note: these example solutions mention first names instead of full names. This is not representative of the actual expected
output.
"""

from datetime import date

from faker.typing import SeedType

import generate_data
from header_print import header_print

"""
We start you off with some random data to parse. Please replace the value of the `your_favourite_food` variable with
your own favourite food. This makes everyone's data unique.

PS: We assume that a customer is uniquely defined by their name. If "Martin Adams" appears multiple times in the data,
this is the same customer.
"""
print("⚙️ Generating data...")
your_favourite_food: SeedType = "I don't have a favourite dish"

customer_specs = generate_data.CustomerSpecs(num_customers=5_000, min_age=12, max_age=80)
order_specs = generate_data.OrderSpecs(num_orders_per_day=20, start_date=date(2024, 1, 1), end_date=date(2024, 12, 31))
data_string = generate_data.main(customer_specs=customer_specs, order_specs=order_specs, seed=your_favourite_food)

# Print first 100 characters of the data to see what it looks like, which is something like this:
# > Martin Adams ,51,M,Monday 01 January 2024,Bald,20;Victor Barnes,28,M,Monday 01 January 2024,Mohawk,40;...
print("🚀 Data generated correctly!")
print(f"Start of data_string: '{data_string[:100]}'")

"""
Exercise 1
==========
The data is now one big string, which makes it difficult to work with. You will have to parse it into a workable format.
This is what Exercise 1 is focused on. Follow the steps below.
"""
header_print("Exercise 1")

"""
Exercise 1.1
============
The data seems to have multiple orders, which are separated by a semicolon (;).

As the first step, create a list `orders_strings` where each entry is only the string corresponding to one order.
> Example output: ["Martin Adams ,51,M,Monday 01 January 2024,Bald,20", "Victor Barnes,28,M,Monday 01 January 2024,Mohawk,40", ...]
"""
header_print("Exercise 1.1")
orders_strings = ...
# from .solutions.exercise_1_1 import orders_strings


print("🔍 Parsing data...")

# 1. Split the long string into individual records
records = data_string.split(";")

parsed_data = []

for record in records:
    record = record.strip()  # remove leading/trailing spaces
    if not record:
        continue  # skip empty records

    fields = record.split(",")

    # Each record must contain exactly 6 fields
    if len(fields) != 6:
        continue

    # Unpack the fields
    name, age, gender, date_str, hairstyle, order_num = fields

    # Convert the record into a clean dictionary
    parsed_data.append({
        "name": name.strip(),
        "age": int(age),
        "gender": gender.strip(),
        "date": date_str.strip(),
        "hairstyle": hairstyle.strip(),
        "order_num": int(order_num),
    })

print(f"📦 Successfully parsed {len(parsed_data)} records!")

    #Test_to_show_the_resul_tex1.1
print(parsed_data[:1])



"""
Exercise 1.2
============
Now that you have a list of order strings, it starts to look a bit more neat. However, how do you handle an individual
order and get insights from this?

As the next step in the data parsing, each element of the list should be a list itself. Make a new variable and name
it `orders_lists`.
> Example output: [["Martin Adams ", "51", "M", "Monday 01 January 2024", "Bald", "20"], ...]
"""
header_print("Exercise 1.2")
orders_lists = ...
# from .solutions.exercise_1_2 import orders_list

orders_lists = []

for record in records:
    record = record.strip()
    if not record:
        continue

    fields = record.split(",")
    orders_lists.append(fields)


    #Test_to_show_the_result_ex1.2
print("Example:", orders_lists[:3])


orders_dictionary = {}
 
for i in range(len(records)):
    record = records[i]
    record = record.split(',')
    orders_dictionary[i]= {"Name":record[0],
                           "Age": record[1],
                           "Gender": record[2],
                           "Date": record[3],
                           "Hairstyle":record[4],
                           "Order_number":record[5]}
 
print(orders_dictionary)


"""
Exercise 1.3
============
Great, each part of our list is now an individual order that we can use! The next issue pops up though: some names seem
to have some data corruption and they have some whitespaces before or after the name. See for example in our example
output above, that we have the name "Martin Adams " and not "Martin Adams" - this was not a typo ;)

As the next step, go through the list and remove the whitespaces from the start and end of names. Make a new variable
and name it `orders_cleaned`.
> Example output: [["Martin Adams", "51", "M", "Monday 01 January 2024", "Bald", "20"], ...]
"""
header_print("Exercise 1.3")
orders_cleaned = ...
# from .solutions.exercise_1_3 import orders_cleaned

orders_cleaned = []

for order in orders_lists:
    # Copy the order so we don't change the original
    cleaned_order = order.copy()

    # Clean the name (index 0)
    cleaned_order[0] = cleaned_order[0].strip()

    orders_cleaned.append(cleaned_order)



    #Test_to_show_the_result_ex1.3
print("Example:", orders_cleaned[:2])




"""
Exercise 1.4
============
Awesome work! The names now seem to be cleaned and we are ready to go. Or are we? If you take a better look, there is
another issue. Can you spot it...?

Indeed, the integers in the list also seem to be strings. This means that we cannot perform numerical operations on
them, so we need to transform (aka cast) them.

As the next step, go through the orders and make the age of the customer and the price of the hairstyle integer. Make a
new variable and name it `orders_casted`.
> Example output: [["Martin Adams", 51, "M", "Monday 01 January 2024", "Bald", 20], ...]
"""
header_print("Exercise 1.4")
orders_casted = ...
# from .solutions.exercise_1_4 import orders_casted


orders_casted = []

for order in orders_cleaned:
    # Copy the order to avoid changing the original
    casted_order = order.copy()

    # Convert age and order_num to integers
    casted_order[1] = int(casted_order[1])      # age
    casted_order[5] = int(casted_order[5])      # order_num / price

    orders_casted.append(casted_order)



    #Test_to_show_the_result_ex1.4
print("Example:", orders_casted[:3])


"""
Exercise 2
==========
Congratulations! The data is now in a workable format and we can move on to the exciting part: extracting insights
from the data. Let's start with getting to know the data a little bit better.

For each sub-exercise, print it in the format: "Customer <name> got the haircut <hairstyle> on <date> for €<cost>.".
> Example output:
> "Customer Natalie Adams got the haircut Braided on Monday 30 December 2024 for €42.00."
> "Customer Caroline Barnes got the haircut Bald on Tuesday 31 December 2024 for €20.00."
> "Customer Glenn Collier got the haircut Pompadour on Tuesday 31 December 2024 for €38.00."
"""
header_print("Exercise 2")

"""
Exercise 2.1
============
What were the first 3 orders?
"""
header_print("Exercise 2.1")
orders_first_3 = ...

orders_first_3 = orders_casted[:3]  # take the first 3 orders

# Print them in the required format
for order in orders_first_3:
    name = order[0]
    hairstyle = order[4]
    date = order[3]
    price = order[5]
    print(f"Customer {name} got the haircut {hairstyle} on {date} for €{price:.2f}.")


"""
Exercise 2.2
============
What were the last 5 orders?
"""
header_print("Exercise 2.2")
orders_last_5 = ...


orders_last_5 = orders_casted[-5:]  # take the last 5 orders

# Print them in the required format
for order in orders_last_5:
    name = order[0]
    hairstyle = order[4]
    date = order[3]
    price = order[5]
    print(f"Customer {name} got the haircut {hairstyle} on {date} for €{price:.2f}.")


"""
Exercise 2.3
============
What was the 1000th order?
"""
header_print("Exercise 2.3")
order_1000 = ...



order_1000 = orders_casted[999]  # 1000th order (index 999)

# Print in the required format
name = order_1000[0]
hairstyle = order_1000[4]
date = order_1000[3]
price = order_1000[5]

print(f"Customer {name} got the haircut {hairstyle} on {date} for €{price:.2f}.")


"""
Exercise 2.4
============
What were the 2000th until 2025th orders?
"""
header_print("Exercise 2.4")
order_2000_to_2025 = ...

order_2000_to_2025 = orders_casted[1999:2025]  # orders 2000 to 2025 (inclusive)

# Print them in the required format
for order in order_2000_to_2025:
    name = order[0]
    hairstyle = order[4]
    date = order[3]
    price = order[5]
    print(f"Customer {name} got the haircut {hairstyle} on {date} for €{price:.2f}.")



"""
Exercise 3
==========
Of course, customers do not only get one haircut per year, so you expect to see some names in the data multiple times
(remember that we assume that the name of a customer is unique).

Find the unique customers that the hairdresser has served. Put the unique names in a variable called `unique_names`, and
then print how many there are in and who they are in this format: "There are ... unique names, namely ..."
> Example output: "There are 637 unique names, namely ['Terry Adams', 'Dennis Barnes', 'Beth Collier', ..."

Extra challenge: Try this with a set comprehension!

"""
header_print("Exercise 3")
unique_names = ...


# Use a set comprehension to get unique names
unique_names = [order[0].split()[0]for order in orders_casted]
unique_names = set(unique_names)

# Convert to list if you want ordered printing (optional)
unique_names_list = list(unique_names)

print(f"There are {len(unique_names)} unique names, namely {unique_names_list}")


#Show the unique names vertically and count the times in addition to oredering A - Z

from collections import Counter

# 1. Extract all names
all_names = [order[0].split()[0] for order in orders_casted]

# 2. Count occurrences
name_counts = Counter(all_names)

# 3. Sort names alphabetically
for name in sorted(name_counts):
    print(f"{name} — {name_counts[name]}")


"""
Exercise 4
==========
The hairdresser would like to know how much revenue they made. Try to find the following and print the results:
"""
header_print("Exercise 4")

"""
Exercise 4.1
============
What was the total revenue in the data? Put this in a variable named `total_revenue`.
"""
header_print("Exercise 4.1")
total_revenue = ...

# We want to calculate the total revenue
# First, we start with 0
total_revenue = 0

# Go through each order in the list
for order in orders_casted:
    # Add the price of this order to total_revenue
    total_revenue += order[5]

# Print the total revenue
print("Total revenue: €", total_revenue)



"""
Exercise 4.2
============
What was the revenue in the month of March 2024? Put this in a variable named `revenue_march_2024`.
"""
header_print("Exercise 4.2")
revenue_march_2024 = ...



# We want revenue only for March 2024
# Start with 0
revenue_march_2024 = 0

# Go through each order
for order in orders_casted:
    # Check if the order is in March 2024
    if "March 2024" in order[3]:
        # Add the price to the revenue
        revenue_march_2024 += order[5]

# Print the revenue for March 2024
print("Revenue in March 2024: €", revenue_march_2024)


"""
Exercise 4.3
============
What was the revenue on Mondays? What about on Sundays? Name these variables `revenue_mondays` and `revenue_sundays`.
"""
header_print("Exercise 4.3")
revenue_mondays = ...
revenue_sundays = ...

# We want to know the revenue on Mondays and Sundays
revenue_mondays = 0
revenue_sundays = 0

# Go through each order
for order in orders_casted:
    # Check if the order was on Monday
    if "Monday" in order[3]:
        revenue_mondays += order[5]
    # Check if the order was on Sunday
    elif "Sunday" in order[3]:
        revenue_sundays += order[5]

# Print the results
print("Revenue on Mondays: €", revenue_mondays)
print("Revenue on Sundays: €", revenue_sundays)


"""
Exercise 4.4
============
The hairdresser would like to know the revenue per gender. They would also like to know how many orders were made per
gender, because they are interested in knowing the average order price per gender (rounded to 2 decimals).

You may assume that every customer's gender is one of M, F, or X.

For each gender, print in the following format:
> "Revenue <gender>: <revenue> (<count> clients). Average revenue: €<average_revenue>."
> Example output: Revenue M: €91,252.00 (2356 clients). Average revenue: €38.73.

Extra challenge: try to use only one for-loop to compute the necessary information for all genders.
"""
header_print("Exercise 4.4")
revenue_m = 0
revenue_f = 0
revenue_x = 0


count_m = 0
count_f = 0
count_x = 0

# Go through each order once
for order in orders_casted:
    gender = order[2]  # gender is at index 2
    price = order[5]   # price is at index 5

    if gender == "M":
        revenue_m += price
        count_m += 1
    elif gender == "F":
        revenue_f += price
        count_f += 1
    elif gender == "X":
        revenue_x += price
        count_x += 1

# Calculate average revenue per gender, rounded to 2 decimals
average_m = round(revenue_m / count_m, 2) if count_m != 0 else 0
average_f = round(revenue_f / count_f, 2) if count_f != 0 else 0
average_x = round(revenue_x / count_x, 2) if count_x != 0 else 0

# Print results in the required format
print(f"Revenue M: €{revenue_m:.2f} ({count_m} clients). Average revenue: €{average_m:.2f}.")
print(f"Revenue F: €{revenue_f:.2f} ({count_f} clients). Average revenue: €{average_f:.2f}.")
print(f"Revenue X: €{revenue_x:.2f} ({count_x} clients). Average revenue: €{average_x:.2f}.")



"""
Exercise 4.5
============
Every year. the Institute of Statistics Netherlands (ISN) is doing research into the inflation trends in the
Netherlands. To do so, they collect data from as many hairdressers in the Netherlands as possible. Therefore, they have
reached out to you. They want to know the average price of a haircut.

Calculate the average price of a haircut and print the result in the following format:
> "Average price of a haircut: €<average_price_haircut>."

For this calculation, you can use the variable HAIRSTYLES, which is a list of tuples. The first element of each tuple is
the name of the haircut, the second element is the price. You can print it to inspect it.
"""


header_print("Exercise 4.5")
HAIRSTYLES = generate_data.HAIRSTYLES
print(f"{HAIRSTYLES=}")

average_price_haircut = 0

# Sum all haircut prices
total_price = 0
for style in HAIRSTYLES:
    # style is a tuple like ("Bald", 20)
    price = style[1]
    total_price += price

# Calculate the average price
average_price_haircut = total_price / len(HAIRSTYLES)

# Print the result
print(f"Average price of a haircut: €{average_price_haircut:.2f}.")



"""
Exercise 4.6
============
The ISN finally publishes its research results on the inflation trends in the Netherlands of the past year. In the last
chapter of the research report, the hairdresser reads that the average inflation is 3.5%. This means that, on average,
the cost of living has increased by 3.5%. To compensate for this, the hairdresser wants to increase the prices of
haircuts by 3.5%; however, only for the working class. This way, juniors (<18) and seniors (>65) will not be affected.
The hairdresser wants to know want the impact on the revenue would have been last year if they had raised their prices
by 3.5% last year already.

Apply the price change of 3.5% on the working class and calculate the new revenue. Name this new revenue variable
`total_revenue_inflation_correction`.

Print the result in the following format:
> "Revenue after price change: €<total_revenue_inflation_correction>."
"""

header_print("Exercise 4.6")
total_revenue_inflation_correction = 0

# Loop through all orders
for order in orders_casted:
    age = order[1]
    price = order[5]

    # Apply price increase only for working class (18-65)
    if 18 <= age <= 65:
        new_price = price * 1.035   # increase by 3.5%
    else:
        new_price = price           # juniors and seniors unchanged

    # Add to the corrected revenue
    total_revenue_inflation_correction += new_price

# Print the result
print(f"Revenue after price change: €{total_revenue_inflation_correction:.2f}.")


"""
Exercise 4.7
============
Well done! The hairdresser now wants to know difference in revenue if they actually had raised the prices of the
haircuts by 3.5% for the working class last year. Calculate the difference between the actual revenue (`total_revenue`)
and the predicted revenue after inflation correction (`total_revenue_inflation_correction`) and name this variable
`revenue_difference`.

Print the output in the following format:
> "Revenue increase after inflation correction: €<revenue_difference>."
"""
header_print("Exercise 4.7")
# from .solutions.exercise_4_1 import total_revenue
# from .solutions.exercise_4_6 import total_revenue_inflation_correction
revenue_difference = ...

revenue_difference = total_revenue_inflation_correction - total_revenue

print(f"Revenue increase after inflation correction: €{revenue_difference:.2f}.")


"""
Exercise 4.8
============
The hairdresser is surprised! So much extra revenue. However, it just doesn't sit and feel right. The hairdresser wants
to know if they can afford to give some discount to juniors and seniors without losing the extra revenue due to the
price increase on the working class. The hairdresser decides to give a 10% discount to juniors and a 5% discount
to seniors (while still applying the 3.5% price increase on the working class).

Calculate the new revenue after this and call this revenue `total_revenue_discount`. Print the output in the following
format:
> "Revenue after discount: €<total_revenue_discount>."
"""

header_print("Exercise 4.8")
total_revenue_discount = 0

for order in orders_casted:
    age = order[1]
    price = order[5]

    # Working class: +3.5%
    if 18 <= age <= 65:
        new_price = price * 1.035

    # Juniors: -10%
    elif age < 18:
        new_price = price * 0.90

    # Seniors: -5%
    else:  # age > 65
        new_price = price * 0.95

    total_revenue_discount += new_price

print(f"Revenue after discount: €{total_revenue_discount:.2f}.")


"""
Exercise 4.9
============
Calculate the difference in revenue again. However, this time, calculate the percentual increase and name the variable
`revenue_difference_percent`. Print the output in the following format:
> "Percentual revenue increase after discount: <revenue_difference_percent>%."
"""


header_print("Exercise 4.9")
# from .solutions.exercise_4_8 import total_revenue_discount
revenue_difference_percent = (
    (total_revenue_discount - total_revenue) / total_revenue
) * 100

print(f"Percentual revenue increase after discount: {revenue_difference_percent:.2f}%.")



"""
Exercise 4.10
============
Nice! The hairdresser will actually make <revenue_difference_percent>% more revenue the coming year with the planned
discounts for juniors and seniors, and the price increase for the working class. However, the hairdresser knows that the
Wavy haircut is very popular among juniors. Therefore, the hairdresser wishes to exclude this haircut from the discount
for juniors.

Calculate the new revenue after without the discount for the Wavy haircut for juniors and call this revenue
`total_revenue_discount_no_wavy`. Print the output in the following format:
> "Revenue after discount (no Wavy): €<total_revenue_discount_no_wavy>."
"""

header_print("Exercise 4.10")
total_revenue_discount_no_wavy = 0

for order in orders_casted:
    age = order[1]
    price = order[5]
    hairstyle = order[4]

    # Working class → +3.5%
    if 18 <= age <= 65:
        new_price = price * 1.035

    # Juniors → normally -10%, but Wavy has no discount
    elif age < 18:
        if hairstyle == "Wavy":
            new_price = price       # no discount
        else:
            new_price = price * 0.90

    # Seniors → -5%
    else:
        new_price = price * 0.95

    total_revenue_discount_no_wavy += new_price

print(f"Revenue after discount (no Wavy): €{total_revenue_discount_no_wavy:.2f}.")


"""
Exercise 5
==========
"""
header_print("Exercise 5")

"""
Exercise 5.1
============
The hairdresser is very happy with the data analysis so far and wishes to do this every year once the ISN research
results are out. To make this easier, the hairdresser would like to write a function that takes the list of orders as
input and returns the revenue. Write a function to do so. The function should be called `calculate_revenue` and takes
as input a list of orders and returns the total revenue.

Test the function on the original input, `orders_casted`, and see if you get the same revenue as calculated before
(`total_revenue`). Print the results in the following format:
> "Total revenue: <total_revenue>, Total revenue with function: <total_revenue_function>".
"""
header_print("Exercise 5.1")
total_revenue_function = 0

header_print("Exercise 5.1")

def calculate_revenue(orders):
    total = 0
    for order in orders:
       
        price = order[5]
        total += price
    return total

# Select fourmela orders_casted
total_revenue_function = calculate_revenue(orders_casted)

#Print Result
print(f"Total revenue: {total_revenue}, Total revenue with function: {total_revenue_function}.")


"""
Exercise 5.2
============
So far, so good! Now the hairdresser wishes to include a scaling factor as input to the function. This scaling factor
will be applied to all orders. The scaling factor will reflect a price decrease/increase. For example, for a price
decrease of 5% we would input `scaling_factor=0.95` to the function, and for a price increase of 5% we would input
`scaling_factor=1.05`. Write this function!

Test the function on the original orders, `orders_casted`, with scaling factor for an increase of 7.5% and print the
result in the following format:
> "Revenue with scaling factor <scaling_factor> is <total_revenue_scaling_factor>".
"""
header_print("Exercise 5.2")
total_revenue_scaling_factor =0


def calculate_revenue_scaled(orders, scaling_factor):
    total = 0
    for order in orders:
        price = order[5]          # price is the 6th element
        total += price * scaling_factor
    return total

scaling_factor = 1.075
total_revenue_scaling_factor = calculate_revenue_scaled(orders_casted, scaling_factor)

print(f"Revenue with scaling factor {scaling_factor} is {total_revenue_scaling_factor}.")



"""
Exercise 6
==========
The hairdresser wants to attract more customers in a fun way. The hairdresser decides to reward the first customer that
results in a total revenue passing the €1,000.00. Who was this customer in the original `orders_casted` list? When you
have found the lucky customer, print the following:
> "Reached revenue of €1,000.00. {name} is the lucky one! 🎉"

NB: You can assume the list `orders_casted` is sorted, meaning the first row is the first order, and the second row is
the second order, etc.
"""
header_print("Exercise 6")


running_total = 0
winner = None

for order in orders_casted:
    price = order[5]       # price is the last element
    running_total += price

    if running_total >= 1000:
        winner = order[0]  # customer name
        break

print(f"Reached revenue of €1,000.00. {winner} is the lucky one! 🎉")

