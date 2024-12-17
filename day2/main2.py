def is_safe_report(levels):
    def check_levels(levels):
        increasing = all(levels[i] < levels[i + 1] and 1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
        decreasing = all(levels[i] > levels[i + 1] and 1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
        return increasing or decreasing

    if check_levels(levels):
        return True

    for i in range(len(levels)):
        if check_levels(levels[:i] + levels[i+1:]):
            return True

    return False

safe_reports_count = 0

with open("day2/input.txt", "r") as file:
    for line in file:
        # Split the line into individual numbers and convert them to integers
        levels = list(map(int, line.split()))
        
        # Check if the report is safe
        if is_safe_report(levels):
            safe_reports_count += 1

print("Number of safe reports:", safe_reports_count)