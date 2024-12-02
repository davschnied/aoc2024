def line_is_safe(line):
    diffs = []
    sum_of_signs = 0
    for i in range(len(line)-1):
        diff = line[i+1]-line[i]
        diffs.append(diff)
        if diff != 0:
            sum_of_signs += diff/abs(diff)
        else:
            sum_of_signs += 0
    sign = sum_of_signs/abs(sum_of_signs) if sum_of_signs != 0 else 1
    is_safe = True
    for i, diff in enumerate(diffs):
        if abs(diff)<1 or abs(diff)>3 or diff/sign<0:
            return False, i
    return True, None


safe_lines = 0
with open('2/data.txt','r') as data_file:
    for line in data_file:
        this_line = [int(i) for i in line.split()]

        is_safe, level = line_is_safe(this_line)

        if not is_safe:
            new_line = this_line.copy()
            new_line.pop(level)
            is_safe_left, _ = line_is_safe(new_line)
            new_line = this_line.copy()
            new_line.pop(level+1)
            is_safe_right, _ = line_is_safe(new_line)
            if is_safe_left or is_safe_right:
                safe_lines += 1
        else:
            safe_lines += 1


print(safe_lines)