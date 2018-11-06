def paths(graph, v):
    """Generate the maximal cycle-free paths in graph starting at v.
    graph must be a mapping from vertices to collections of
    neighbouring vertices.

    >>> g = {1: [2, 3], 2: [3, 4], 3: [1], 4: []}
    >>> sorted(paths(g, 1))
    [[1, 2, 3], [1, 2, 4], [1, 3]]
    >>> sorted(paths(g, 3))
    [[3, 1, 2, 4]]

    """
    path = [v]                  # path traversed so far
    seen = {v}                  # set of vertices in path
    def search():
        dead_end = True
        for neighbour in graph[path[-1]]:
            if neighbour not in seen:
                dead_end = False
                seen.add(neighbour)
                path.append(neighbour)
                yield from search()
                path.pop()
                seen.remove(neighbour)
        if dead_end:
            yield list(path)
    yield from search()



def f():
	nm = input().strip().split()
	n = int(nm[0])
	m = int(nm[1])
	
	lines = []
	
	for i in range(m):
		l = input().strip().split()
		l = [int(i) for i in l]
		lines.append(l)
	print(lines)

	# each line contains two integers a and b, 
	# if a > 0 there's a directed edge between a and b thats NOT forced
	# if a < 0 there's a directed edge between -a and b that IS forced

	D = {} # edge : [[neighbor,1 (forced)], [neighbor, 0 (not forced)], etc ]
	for i in range(n):
		D[i+1] = []
	print(D)	
	 
	for combo in lines:
		a = combo[0]
		b = combo[1]
		L = []
		L.append(b)
		if a < 0:
			L.append(True)
		elif a > 0:
			L.append(False)
		
		a = abs(a)
		if a in D:		
			L2 = D[a]
			L2.append(L)
			L = L2
		D[a] = L
			
	noReds = []
	for node in D:
		flag = True
		for neighbor in D[node]:
			if neighbor[1] == True:
				flag = False
		if flag:
			noReds.append(node)
	
	# for these, count the min black to get there
	# if min black <= 1, counts as ending node
	

	allpath = bfs_connected_component(D,1)

	print(allpath)









	

f()
