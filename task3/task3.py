import sys
from io import StringIO
import csv
import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[%(asctime)s: %(levelname)s] %(message)s"))
logger.addHandler(handler)


def generate_map(parsed_csv):
    result = {}
    for pair in parsed_csv:
        if len(pair) != 2:
            logger.error(f"{pair} не является парой вершин")
            sys.exit(1)
        try:
            a = int(pair[0])
            b = int(pair[1])
        except ValueError:
            logger.error(f"Вершины {pair} оказались не числами")
            sys.exit(1)
        if a not in result.keys():
            result[a] = set()
        result[a].add(b)
        if b not in result.keys():
            result[b] = set()
        result[b].add(a)
    logger.debug(f"parsed_map = {result}")
    return result


def dfs(v, d, pr, mapa, depth_map, result):
    depth_map[v] = d
    for son in mapa[v]:
        if son not in depth_map.keys():
            if pr != -1:
                result[2].add(pr)
                result[3].add(son)
            dfs(son, d + 1, v, mapa, depth_map, result)


def task(input_str: str):
    reader = csv.reader(StringIO(input_str), delimiter=',')
    mapa = generate_map([row for row in reader])
    depth_map = {}
    result = [set() for i in range(5)]
    dfs(1, 1, -1, mapa, depth_map, result)
    for key, value in mapa.items():
        if key != 1:
            result[1].add(key)
        if len(value) != 1:
            result[0].add(key)
    depth_map_reversed = {}
    for key, value in depth_map.items():
        if value not in depth_map_reversed.keys():
            depth_map_reversed[value] = set()
        depth_map_reversed[value].add(key)
    for key, value in depth_map_reversed.items():
        if len(value) > 1:
            for v in value:
                result[4].add(v)
    result = [[el for el in result[i]] for i in range(5)]
    logger.debug(f"result = {result}")
    return result

