import networkx as nx
def bipartite_minimum_vertex_cover(G:nx.Graph):

    M = nx.algorithms.bipartite.matching.maximum_matching(G)
    L = [k for k,v in G.nodes.items() if v['bipartite'] == 0]
    R = [k for k,v in G.nodes.items() if v['bipartite'] == 1]
    U = set(L) - set(M.keys())


    def bfs_alternating_paths(v, Z, find_match=False):
        Z.add(v)
        u = M[v] if v in M.keys() else None
        if find_match and u:
            bfs_alternating_paths(u, Z, find_match=False)
        elif not find_match:
            unmactched_neibors = [n for n in G.neighbors(v) if n != u]
            for n in unmactched_neibors:
                bfs_alternating_paths(n, Z, find_match=True)
        return

    Z = set()
    for u in U:
        bfs_alternating_paths(u, Z, find_match=False)

    K = set(L) - Z | set(R) & Z
    return K