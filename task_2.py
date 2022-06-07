def return_arr(graph, start, path = []):
    path.append(start)
    if start in graph:
        for elem in graph:
            if graph[elem] not in path:
                for el in graph[elem]:
                    if el not in path:
                        path.append(el)
    return path

def my_code(graph, start):
    path = return_arr(graph, start)
    print(*path, sep='\n')

data1 = {
 1: [2, 3],
 2: [4]
}
data2 = {
 1: [2, 3],
 2: [3, 4],
 4: [1]
}
my_code(data1, 1)
my_code(data2, 1)
