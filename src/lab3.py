def is_equal_x_and_0_count(input_str):
    x_count = 0
    o_count = 0

    input_str = input_str.lower()
    for char in input_str:
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1

    return x_count == o_count

#asdas[""] = asdg


#examples:
input_string = "oOXx"
print(is_equal_x_and_0_count(input_string))

input_string = "xooxx"
print(is_equal_x_and_0_count(input_string))

input_string = "ooxxm"
print(is_equal_x_and_0_count(input_string))

input_string = "zpzpzpp"
print(is_equal_x_and_0_count(input_string))

input_string = "zzoo"
print(is_equal_x_and_0_count(input_string))
