graph ={ 'a':{'b':4,'c':3},
		'b':{'a':4,'e':12,'f':5},
		'c':{'a':3,'e':10,'d':7,},
		'd':{'c':7,'e':2},
		'e':{'b':12,'c':10, 'd':2,'z':5},
		'f':{'b':5,'z':16},
		'z':{'e':5,'f':16}}

def dijksta(map, start, finish):
	shortest_distance={} #record the cost to reach to a certain node and going to be updated as we move donw the path:
	track_predecesor={} #gtrack the path that lead us down that node 
	unseennodes = map  #iterate through the graph
	infinte = 99999 #infinte can be considered a very large number 
	track_path= [] #trace our journy back to the source node which is the fastet route 
	for node in unseennodes:
		shortest_distance[node] = infinte
	shortest_distance[start]=0
	
	while unseennodes :
		min_distance_node = None
		for node in unseennodes:
			if min_distance_node is None:
				min_distance_node = node
			elif shortest_distance[node] < shortest_distance[min_distance_node]:
				min_distance_node= node
		path_option = unseennodes[min_distance_node].items()

		for child_node, weight in path_option:
			if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
				shortest_distance[child_node]= weight + shortest_distance[min_distance_node]
				track_predecesor[child_node] = min_distance_node

		unseennodes.pop(min_distance_node)
	currentnode = finish
	while currentnode != start:
		try:
			track_path.insert(0,currentnode)
			currentnode = track_predecesor[currentnode]
		except KeyError:
			print('Path is not reachable')
			break
	track_path.insert(0,start)


	if shortest_distance[finish]!= infinte:
		print("Shortest path" +str(shortest_distance[finish]))
		print("Optimal path is" +str(track_path))












dijksta(graph, 'a','z')