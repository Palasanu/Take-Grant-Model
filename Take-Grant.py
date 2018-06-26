import pdb

def stare_initiala():
	# graf = {'A':[['B','t'],['C','t']],
	# 		'B':[['C','g']],
	# 		'D':[['a','r','w']],
	# 		'F':[['A','t']],
	# 		'G':[['B','t','g']],
	# 		'H':[['B','g']]}

	graf = {'A':[['x','r','w']],
			'B':[['A','g']],
			'C':[['B','t']],
			'd':[['C','t']],
			'E':[['C','t']],
			'F':[['E','g'],['C','t']],
			'G':[['d','t'],['H','t']],
			'H':[['y','r']]
			}
	return graf

def print_graf(graf):
	for item,val in graf.items():	
		for value in val:
			print (item + " -", end = '')
			for i in range(1,len(value)):
				print (value[i], end = '')
			print ("-> " + value[0])

def who_takes(x, graf):
	nodes = list()
	for item,val in graf.items():
		for value in val:
			if(value[0] == x):
				for i in range(1, len(value)):
					if value[i] == 't':
						nodes.append(item)
	if len(nodes)==0:
		return False
	else:
		return nodes

def who_grats(x,graf):
	nodes = list()
	for item,val in graf.items():
		for value in val:
			if(value[0] == x):
				for i in range(1, len(value)):
					if value[i] == 'g':
						nodes.append(item)
	if len(nodes)==0:
		return False
	else:
		return nodes

def grants(x,graf):
	nodes = list()
	for item,val in graf.items():
		if item == x:
			for value in val:
				for i in range(1, len(value)):
					if value[i] == 'g':
						nodes.append(value[0])
	if len(nodes)==0:
		return False
	else:
		return nodes

def takes(x,graf):
	nodes = list()
	for item,val in graf.items():
		if item == x:
			for value in val:
				for i in range(1, len(value)):
					if value[i] == 't':
						nodes.append(value[0])
	if len(nodes)==0:
		return False
	else:
		return nodes

def is_node_with(right,y,graf):
	nodes= list()
	for item,val in graf.items():
		for value in val:
			if(value[0] == y):
				for i in range(1, len(value)):
					if value[i]==right:
						nodes.append(item)
	return nodes


def noduri_intinde_terminal(y,graf,nodes):
	nodes_that_take = who_takes(y, graf)
	if(nodes_that_take != False):
		for nod in nodes_that_take:
			nodes.append(nod)
			noduri_intinde_terminal(nod,graf,nodes)
	return nodes

def noduri_intind_terminal(x,graf,nodes):
	nodes_take = takes(x, graf)
	if(nodes_take != False):
		for nod in nodes_take:
			nodes.append(nod)
			noduri_intind_terminal(nod,graf,nodes)
	return nodes

def noduri_itinde_initial(y,graf):
 	nodes = set()
 	nodes_that_grant = who_grats(y,graf)
 	if nodes_that_grant != False:
	 	for nod in nodes_that_grant:
	 		nodes.update(noduri_intinde_terminal(nod,graf,list()))
 	nodes = list(nodes)
 	if(len(nodes) > 0):
 		return nodes;
 	else:
 		return False

def is_subject(x):
	if x.isupper():
		return True
	else:
		return False

def is_island(x,graf,island):
	if is_subject(x):
		island.add(x)
	for item,val in graf.items():
		for value in val:
			if (is_subject(value[0]) and item==x):
				if value[0] not in island:
					is_island(value[0],graf,island)
			if(value[0]==x and is_subject(item)):
				if item not in island:
					is_island(item,graf,island)	
	return island

def is_bridge(x,y,graf):
	if x == y:
		return True
	elif x in noduri_intinde_terminal(y,graf,list()):
		return True
	elif y in noduri_intinde_terminal(x,graf,list()):
		return True
	noduri = noduri_intind_terminal(y,graf,list())
	if noduri !=False:
		for nod in noduri:
			noduri = who_grats(nod,graf)
			if(noduri != False):
				for nod_grant in noduri:
					if x in noduri_intinde_terminal(nod_grant,graf,list()):
						return True
	noduri = noduri_intind_terminal(y,graf,list())
	if noduri !=False:
		for nod in noduri:
			noduri = grants(nod,graf)
			if(noduri != False):
				for nod_grant in noduri:
					if x in noduri_intinde_terminal(nod_grant,graf,list()):
						return True

	return False

def check_arc(right,x,y,graf):
	for item,value in graf.items():
		if(item == x and value[0]== y):
			for i in range(1,len(value)):
				if value[i] == right:
					return True
	return False

def can_share(right,x,y,graf):
	if check_arc(right,x,y,graf):
		return True
	s = is_node_with(right,y,graf)
	if(len(s)<=0):
		return False
	noduri = noduri_intinde_terminal(s,graf,list())
	if noduri != False:
		if x in noduri:
			return True
	if s in noduri_intinde_terminal(x,graf,list()):
		return True
	noduri_x = noduri_itinde_initial(x,graf)
	#print (noduri_x)
	if(noduri_x != False):
		noduri_s = list()
		for nod in s:
			noduri_s.extend(noduri_intinde_terminal(nod,graf,list()))
		#print(noduri_s)
		if noduri_s!=False:
			for nod_x in noduri_x:
				for nod_s in noduri_s:
					if(is_bridge(nod_x,nod_s,graf)):
			 			return True

	return False

def can_share2(right,x,y,graf):
	if check_arc(right,x,y,graf):
		return True
	s = is_node_with(right,y,graf)
	if(len(s)<=0):
		return False
	return is_bridge(x,s,graf)


graf = stare_initiala()
noduri = list()
print_graf(graf)
print (can_share('r','B','y',graf))
#print (noduri_itinde_initial('A',graf))
#print (noduri_intinde_terminal('B',graf,noduri))
#print(who_grats('B',graf))
#print(noduri_intind_terminal('E',graf,list()))
#print (is_bridge('C','G',graf))
#print(is_node_with('r','y',graf))
#print(noduri_intinde_terminal('H',graf,list()))
print(is_island('G',graf,set()))