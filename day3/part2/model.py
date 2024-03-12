class EngineSchematics:
    PERIMETER = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, schematic):
        self.schematic_matrix = [list(line) for line in schematic.split("\n")]

    def is_symbol(self, char):
        return not (char.isdigit() or char == ".")

    def is_gear(self, symbol):
        if not (symbol == "*"):
            return False
        else:
            pass

    def is_valid_part(self, part):
        pass

    def valid_parts_sum(self):
        total_parts = 0
        for line, row in enumerate(self.schematic_matrix):
            col = 0
            while col < len(row):
                char = row[col]
                if char.isdigit():
                    i = col
                    number = ""
                    while row[i].isdigit():
                        number += row[i]
                        i += 1
                    part = (line, col, number)
                    if self.is_valid_part(part):
                        total_parts += int(number)
                    
                

        # number = ""
        # for line in self.schematic_matrix:
        #     pass
        # part = {"line_id": line_id, "position": position, "value": number}
        # self.valid_parts.append(part)
