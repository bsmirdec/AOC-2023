with open("day1/calibration.txt", "r") as calibration:
    instructions = calibration.readlines()
    total = 0
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for instruction in instructions:
        first = ""
        last = ""
        digits = []

        for i in range(len(instruction)):
            carac = instruction[i]
            if carac.isdigit():
                if first == "":
                    first = carac
                else:
                    last = carac
            else:
                current_word = ""
                detail = enumerate(instruction[i:])
                for index, letter in detail:
                    current_word += letter
                    if current_word in numbers:
                        if first == "":
                            first = str(numbers.index(current_word))
                            current_word = ""
                        else:
                            last = str(numbers.index(current_word))
                            current_word = ""
        if last:
            number = first + last
        else:
            number = 2*first

        total = total + int(number)
    print(total)
