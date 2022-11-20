import json
import numpy as np


def task(ranking_str_1: str, ranking_str_2: str) -> str:
    try:
        ranking1 = json.loads(ranking_str_1)
        ranking2 = json.loads(ranking_str_2)
    except json.decoder.JSONDecodeError:
        print("Входные данные функции task5 должны быть json-строками")
        exit(1)

    y_a = _get_relationship_matrix(ranking1)
    y_a_t = y_a.transpose()

    y_b = _get_relationship_matrix(ranking2)
    y_b_t = y_b.transpose()

    y_a_b = np.multiply(y_a, y_b)
    y_a_b_t = np.multiply(y_a_t, y_b_t)

    conflicts = []
    for i in range(y_a_b.shape[0]):
        for j in range(y_a_b.shape[1]):
            if y_a_b[i, j] == 0 and y_a_b_t[i, j] == 0:
                if (str(j + 1), str(i + 1)) not in conflicts:
                    conflicts.append((str(i + 1), str(j + 1)))
    return json.dumps(conflicts)


def _get_relationship_matrix(ranking):
    ranks = dict()
    rank_len = _get_ranking_length(ranking)
    for i, rank in enumerate(ranking):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i + 1] <= ranks[j + 1] else 0 for j in range(rank_len)] for i in range(rank_len)],
                     dtype=np.uint8)


def _get_ranking_length(ranking):
    length = 0
    for i in ranking:
        if type(i) is str:
            length += 1
        else:
            length += len(i)
    return length


def main():
    res = task('["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]', '[["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]')
    print(f"Ответ: {res}")


if __name__ == "__main__":
    main()
