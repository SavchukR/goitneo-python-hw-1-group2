from datetime import datetime
from task_1 import get_birthdays_per_week

def main():
    """
        Run test on function `get_birthdays_per_week`
    """

    sample = [ 
        {"name": "NO Bill Gates", "birthday": datetime(1955, 10, 28)},
        {"name": "NO Gummy Karter", "birthday": datetime(1915, 2, 10)},
        {"name": "YES Geremy Goor", "birthday": datetime(1952, 2, 26)},
        {"name": "YES Geremy Evans", "birthday": datetime(1952, 2, 27)},
        {"name": "YES Geremy Gates", "birthday": datetime(1952, 2, 28)},
        {"name": "YES Karter Gates", "birthday": datetime(1960, 2, 29)},
        {"name": "YES Karter Gates", "birthday": datetime(1957, 3, 1)},
        {"name": "YES weekend Lily Gates", "birthday": datetime(1957, 3, 2)},
        {"name": "YES weekend Lily Evans", "birthday": datetime(1904, 3, 3)},
        {"name": "NO Bill Evans", "birthday": datetime(1904, 3, 4)}
    ]
    
    print()
    print("{0:+^30} {1:^20} {2:+^30}".format("+","Test sample","+"))
    print()
    print(f"Today: {datetime.today()}")
    print()
    print("| {0:-^30} | {0:-^30} |".format("-"))
    print("| {0:^30} | {1:^30} |".format("Name", "Birthday"))
    print("| {0:-^30} | {0:-^30} |".format("-"))
    for row in sample:
        print("| {0:<30} | {1:^30} |".format(row["name"], str(row["birthday"])))
    print("| {0:-^30} | {0:-^30} |".format("-"))
    print()    
    print("{0:+^30} {1:^20} {2:+^30}".format("+","Run","+"))
    print()
    print("Result: ")
    print()
    
    get_birthdays_per_week(sample)

if __name__ == "__main__":
    main()
