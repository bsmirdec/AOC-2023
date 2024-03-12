from day3.part1.masterfunction import validate_parts


with open("day3/exemple.txt", "r") as input:
    # schematics = input.readlines()
    # decode_txt(schematics)

    total = validate_parts(input)

    print(total)
