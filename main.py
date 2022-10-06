from task3 import task3


def main():
    reference = [['1', '2'], ['1', '3'], ['2', '3'], ['2', '4']]
    with open('./data/data2.csv') as file:
        csv_string = file.read()
        result = task3.task(csv_string)
        print(result)


if __name__ == "__main__":
    main()
