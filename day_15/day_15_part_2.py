# https://adventofcode.com/2023/day/15

file_name = "input.txt"
file = open(file_name)

steps = file.readline().split(",")

def get_box(label):
    result = 0
    for c in label:
        result += ord(c)
        result *= 17
        result %= 256
    return result

boxes = [[] for x in range(256)]

def remove_in_box(box, label):
    labels = list(map(lambda label: label[0], boxes[box]))
    if label in labels:
        index = labels.index(label)
        boxes[box].pop(index)

def put_in_box(box, label, focal):
    labels = list(map(lambda label: label[0], boxes[box]))
    if label in labels:
        index = labels.index(label)
        boxes[box][index] = (label, focal)
    else:
        boxes[box].append((label,focal))

def process_step(label, operator, focal):
    box = get_box(label)
    if operator == "-":
        remove_in_box(box, label)
    else:
        put_in_box(box, label, focal)

res = 0
for step in steps:
    if "=" in step:
        operator = "="
        label, focal = step.split("=")
    else:
        operator = "-"
        label = step.split("-")[0]
        focal = None
    process_step(label, operator, focal)

result = 0
for box_index, box in enumerate(boxes):
    if len(box) == 0:
        continue
    for elt_index, elt in enumerate(box):
        res += (box_index + 1) * (elt_index + 1) * int(elt[1])

print(res)