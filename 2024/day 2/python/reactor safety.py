from operator import truediv

from _modules.advent_helpers import strip_linebreak

print("Part 1")
# input of report containing level readings
# report length is infinite
# values are separated by ` ` (space)
# each value in the report must be either ALL increasing or decreasing
# and then must at least change by 1 but not more than 3

# with(open(f"..\\puzzle_input.txt") as f):
#     print("yuh")
#     num_safe_reports = 0
#
#     for report in f.readlines():
#         report_levels = strip_linebreak(report).split(" ")
#         # print(f"{strip_linebreak(report)}")
#         report_check = []
#         report_safe = True
#
#         # find direction and safety check
#         for _ in range(0, len(report_levels) - 1):
#             if abs(int(report_levels[_]) - int(report_levels[_ + 1])) not in range(1,4):
#                 # print("delta unsafe")
#                 report_safe = False
#                 break
#             elif int(report_levels[_]) > int(report_levels[_ + 1]):
#                 # print(f"{report_levels} | {report_levels[_]} --> {report_levels[_ + 1]} | -")
#                 report_check.append("-")
#             elif int(report_levels[_]) < int(report_levels[_ + 1]):
#                 # print(f"{report_levels} | {report_levels[_]} --> {report_levels[_ + 1]} | +")
#                 report_check.append("+")
#
#             for ind in report_check:
#                 if ind != report_check[0]:
#                     # print("trend unsafe")
#                     report_safe = False
#                     break
#
#         if report_safe:
#             # print(f"SAFE\t: {strip_linebreak(report)} | {report_check}")
#             num_safe_reports += 1
#         else:
#             # print(f"UNSAFE\t: {strip_linebreak(report)} | {report_check}")
#             continue
#     print(num_safe_reports)


print("Part 2")
# Part 1 but with tolerance
# Get report levels
# Loop over once
# generate trend list
# generate breaching numbers
# take both through problem dampener pick which one is safe
with(open(f"..\\puzzle_input.txt") as f):
    num_safe_reports = 0
    unsafe_values = []


    def increment_check(report: list[int]):
        bad_increments = []
        for _ in range(0, len(report) - 1):
            if abs(int(report[_]) - int(report[_ + 1])) not in range(1, 4):
                bad_increments.append(_)
                print(_)
        return bad_increments


    def trend_check(report: list[int]):
        bad_trends = []
        _trends = []
        for _ in range(0, len(report) - 1):
            if int(report[_]) > int(report[_ + 1]):
                # print(f"{report_levels} | {report_levels[_]} --> {report_levels[_ + 1]} | -")
                _trends.append("-")
            elif int(report[_]) < int(report[_ + 1]):
                # print(f"{report_levels} | {report_levels[_]} --> {report_levels[_ + 1]} | +")
                _trends.append("+")

        for _ in range(0, len(_trends) - 1):
            if _trends[_] != _trends[_ + 1]:
                print(_)
                bad_trends.append(_)
        return bad_trends


    for report in f.readlines():
        report_levels = strip_linebreak(report).split(" ")
        # print(f"{strip_linebreak(report)}")
        report_check = []
        report_safe = True
        problem_index = []

        problem_index += increment_check(report_levels)
        problem_index += trend_check(report_levels)

        # get rough position of problem index
        for index in range(0, len(problem_index) -1):
            attempt_fix = []
            if abs(problem_index[index]- problem_index[index + 1]) < 2:
                print("diff is 1")
                attempt_fix += increment_check(report_levels.pop(problem_index[max(problem_index[index], problem_index[index] + 1)]))
                attempt_fix += trend_check(report_levels.pop(problem_index[max(problem_index[index], problem_index[index] + 1)]))
                if len(attempt_fix) < len(problem_index):
                    print("a", attempt_fix)
                    report_safe = True
                else:
                    report_safe = False
                    break
            else:
                report_safe = False
                break

        print(problem_index)

        if report_safe:
            # print(f"SAFE\t: {strip_linebreak(report)} | {report_check}")
            num_safe_reports += 1
        else:
            print(f"UNSAFE\t: {strip_linebreak(report)} | {report_check}")
            continue
    print(num_safe_reports)

# 70 65 63 62 61 58 56 53
# 65 63 62 61 58 56 53
#   -2  -1  -1  -3  -2  -3
