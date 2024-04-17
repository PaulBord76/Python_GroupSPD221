input_string = "10591351"
def most_frequent_numbers(input_string):
    num_count = {}

    for num in input_string:
        if num.isdigit():
            num = int(num)
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

    sorted_num_count = dict(sorted(num_count.items(), key=lambda x: x[1], reverse=True))
    most_frequent_numbers = dict(list(sorted_num_count.items())[:3])

    return most_frequent_numbers



result = most_frequent_numbers(input_string)
print(result)
