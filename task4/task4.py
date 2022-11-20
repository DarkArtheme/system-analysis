from io import StringIO
import math
import csv


def task(csv_string):
    f = StringIO(csv_string)
    reader = csv.reader(f, delimiter=',')
    edges = [[int(el) for el in row] for row in reader]
    arr = [[] for i in range(5)]
    # Отношение 1 - прямое управление
    arr[0] = [edge[0] for edge in edges]

    # Отношение 2 - прямое подчинение
    arr[1] = [edge[1] for edge in edges]

    for i in range(len(edges)):
        for j in range(len(edges)):
            if i != j:
                # Отношение 3 - косвенное управление
                if edges[i][1] == edges[j][0]:
                    arr[2].append(edges[i][0])

                # Отношение 4 - косвенное подчинение
                if edges[i][0] == edges[j][1]:
                    arr[3].append(edges[i][1])

                # Отношение 5 - соподчинение
                if edges[i][0] == edges[j][0]:
                    arr[4].append(edges[i][1])

    v_num = max(v for edge in edges for v in edge)
    res_arr = [[] for _ in range(v_num)]
    for v in range(v_num):
        for i in range(5):
            res_arr[v].append(arr[i].count(v + 1))

    return -sum([(x / (v_num - 1)) * math.log(x / (v_num - 1), 2) for row in res_arr for x in row if x != 0])


def main():
    with open("./data/data.csv", "r") as f:
        csv_str = f.read()
    res = task(csv_str)
    print(res)


if __name__ == "__main__":
    main()
