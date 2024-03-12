from masterfunction import validate_parts, decode_txt

with open("day3/input.txt", "r") as input:
    schematic = decode_txt(input)
    valid_parts_sum = validate_parts(schematic)["total_parts"]

    print("total parts: ", valid_parts_sum)
