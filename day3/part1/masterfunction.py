def decode_txt(txt):
    lines = txt.readlines()
    symbols = []
    gears = []
    parts = []
    for i in range(len(lines)):
        line_txt = lines[i]
        line_id = i
        j = 0
        while j < len(line_txt)-1:
            carac = line_txt[j]
            position = j
            if carac != ".":
                if carac.isdigit():
                    k = j
                    number = ""
                    while line_txt[k].isdigit():
                        number += line_txt[k]
                        k += 1
                    part = {"line_id": line_id, "position": position, "value": number, "is_valid": False}
                    parts.append(part)
                    j = k
                else:
                    if carac == "*":
                        gear = (line_id, position)
                        gears.append(gear)
                    symbol = (line_id, position)
                    symbols.append(symbol)
                    j += 1
            else:
                j += 1
    return {"parts": parts, "symbols": symbols, "gears": gears}


def validate_parts(schematic):
    valid_parts = []
    valid_parts_sum = 0
    for part in schematic["parts"]:
        line_id = part["line_id"]
        position = part["position"]
        value = part["value"]
        for i in range(line_id-1, line_id+2):
            for j in range(position-1, position + len(value) + 1):
                if (i, j) in schematic["symbols"]:
                    part["is_valid"] = True
                    if part not in valid_parts:
                        valid_parts.append(part)
                        valid_parts_sum += int(value)
    return {"total_parts": valid_parts_sum, "parts_list": valid_parts}


def validate_gears(input):
    schematic = decode_txt(input)
    matrix = [list(line) for line in input.split("\n")]
    gears_power_sum = 0
    for gear in schematic["gears"]:
        line_id = gear[0]
        position = gear[1]
        near_parts = []
        if (matrix[line_id][position - 1].isdigit() or matrix[line_id][position + 1].isdigit()):
            pass
        else:
            pass