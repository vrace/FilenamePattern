def match_filename_pattern(pattern: str, filename: str):
    if len(pattern) == 0 or len(filename) == 0:
        return (len(pattern) == 0 or pattern == "*") and len(filename) == 0

    if pattern[0] == '?':
        return match_filename_pattern(pattern[1:], filename[1:])
    if pattern[0] == '*':
        for i in range(0, len(filename)):
            if match_filename_pattern(pattern[1:], filename[i:]):
                return True
        return False
    else:
        return pattern[0] == filename[0] and match_filename_pattern(pattern[1:], filename[1:])


def print_match_result(pattern: str, *names):
    print(f"Pattern: {pattern}")
    for name in names:
        print("{}: {}".format(name, "Match" if match_filename_pattern(pattern, name) else "Mismatch"))
    print("+" * 80)


def main():
    print("Filename Pattern Demo")
    print_match_result("ABC_???.txt", "ABC_001.txt", "ABC_002.txt", "ABC_DEF.txt", "AAA_000.txt", "ABC_0.txt", "ABC_0001.txt")
    print_match_result("ABC_*", "ABC_001.txt", "ABC_002.txt", "ABC_DEF.txt", "AAA_000.txt", "ABC_0.txt", "ABC_0001.txt", "ABC_")
    print_match_result("A*?K", "ASK", "ACK", "ASDFGHJK", "AK", "A341?K")
    pass


if __name__ == "__main__":
    main()
