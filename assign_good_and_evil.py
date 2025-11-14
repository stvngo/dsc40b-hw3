from collections import deque

def assign_good_and_evil(graph):

    label = {}  # node -> 'good' or 'evil'
    colors = {0: 'good', 1: 'evil'}

    for start in graph.nodes:
        if start in label:
            continue
        # start a BFS component
        label[start] = colors[0]
        q = deque([start])

        while q:
            u = q.popleft()
            cu = 0 if label[u] == 'good' else 1
            for v in graph.neighbors(u):
                if v not in label:
                    label[v] = colors[1 - cu]
                    q.append(v)
                else:
                    # conflict?
                    if label[v] == label[u]:
                        return None
    return label