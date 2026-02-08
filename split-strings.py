def solution(s):
    input_str = str(s)
    str_n = len(input_str)
    output_list = []
    if (str_n % 2 == 0): 
        for i in range(0, str_n, 2):
            pair = input_str[i] + input_str[i+1]
            output_list.append(pair)
    else:
        for i in range(0, str_n - 1, 2):
            pair = input_str[i] + input_str[i+1]
            output_list.append(pair)
        last_pair = input_str[str_n - 1] + "_"
        output_list.append(last_pair)
    return output_list
