from model import EngineSchematics

def test_valid_parts_sum():
    with open("day3/exemple.txt", "r") as input:
        schematic = input.read()
        engine_schematic = EngineSchematics(schematic)
        print(engine_schematic.schematic_matrix)
        engine_schematic.valid_parts_sum()

    # sum = valid_parts_sum(input)
    # assert sum == 4361


test_valid_parts_sum()