import numpy as np
import json
import csv


def find_ind(el, arr):
    try:
        res = arr.index(el)
    except ValueError:
        res = -1
    return res


def to_list(s):
    try:
        res = [j for j in json.loads(s)]
    except ValueError:
        reader = csv.reader(s.split('\n'), delimiter=',')
        res = [[float(el) for el in row] for row in reader]
    return res


def create_matrix(arr, ind):
    a = arr[ind]
    res = np.zeros((len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                res[i][j] = 1
            if a[i] == a[j]:
                res[i][j] = 0.5
            if a[i] > a[j]:
                res[i][j] = 0
    return res


def task(js):
    arr = to_list(js)
    matrices = [create_matrix(arr, find_ind(el, arr)) for el in arr]
    m = np.zeros(matrices[0].shape)
    for i in range(matrices[0].shape[0]):
        for j in range(matrices[0].shape[0]):
            for k in range(len(matrices)):
                m[i][j] += matrices[k][i][j] / matrices[k].shape[0]
    k0 = [1 / matrices[0].shape[0] for _ in range(matrices[0].shape[0])]
    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1 / l, y)
    while max(abs(k1 - k0)) >= 0.001:
        k0 = k1
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1 / l, y)
    return [round(el, 3) for el in k1]


def main():
    res1 = task('[[1,3,2],[2,2,2],[1.5,3,1.5]]')
    res2 = task("1,3,2\n2,2,2\n1.5,3,1.5")
    print(f"Ответ: res1 = {res1}, res2 = {res2}")


if __name__ == "__main__":
    main()
