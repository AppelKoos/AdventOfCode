from _modules.advent_helpers import strip_linebreak

print("Part 1")
# input of report containing level readings
# report length is infinite
# values are separated by ` ` (space)
# each value in the report must be either ALL increasing or decreasing
# and then must at least change by 1 but not more than 3

with(open(f"..\\puzzle_input.txt") as f):
    print("yuh")
    num_safe_reports = 0

    for report in f.readlines():
        report_levels = strip_linebreak(report).split(" ")
        # print(f"{strip_linebreak(report)}")
        report_check = []
        report_safe = True

        # find direction and safety check
        for _ in range(0, len(report_levels) - 1):
            if abs(int(report_levels[_]) - int(report_levels[_ + 1])) not in range(1,4):
                # print("delta unsafe")
                report_safe = False
                break
            elif int(report_levels[_]) > int(report_levels[_ + 1]):
                # print(f"{report_levels} | {report_levels[_]} --> {report_levels[_ + 1]} | -")
                report_check.append("-")
            elif int(report_levels[_]) < int(report_levels[_ + 1]):
                # print(f"{report_levels} | {report_levels[_]} --> {report_levels[_ + 1]} | +")
                report_check.append("+")

            for ind in report_check:
                if ind != report_check[0]:
                    # print("trend unsafe")
                    report_safe = False
                    break

        if report_safe:
            # print(f"SAFE\t: {strip_linebreak(report)} | {report_check}")
            num_safe_reports += 1
        else:
            # print(f"UNSAFE\t: {strip_linebreak(report)} | {report_check}")
            continue
    print(num_safe_reports)
