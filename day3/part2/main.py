from model import EngineSchematics


def main():
    with open("day3/input.txt", "r") as input:
        schematic = input.read()
        engine_schematic = EngineSchematics(schematic)
    print(engine_schematic.schematic_matrix)


main()
