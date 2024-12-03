import re

def get_next_dont(text):
    result = re.search("don't\(\)", text)
    return result.start() if result is not None else len(text)-1

def get_next_do(text):
    result = re.search("do\(\)", text)
    return result.start() if result is not None else None

def get_result(text):
    result = 0
    x = re.findall("mul\((\d{1,3}),(\d{1,3})\)", text)
    if result is None:
        return 0
    for instr in x:
        result += int(instr[0]) * int(instr[1])
    return result

complete_text = ""
result = 0
with open('3/data.txt','r') as data_file:
    for line in data_file:
        complete_text += line

    text_start = 0
    text_end = 0
    while True:
        text_end = text_start + get_next_dont(complete_text[text_start:])
        result += get_result(complete_text[text_start:text_end])
        next_do = get_next_do(complete_text[text_end:])
        if next_do is None:
            break
        text_start = text_end + next_do

print(result)