class Graph:
    def __init__(self):
        self.number_of_nodes=0;
        self.adjacency_list={}

    def __str__(self):
        return str(self.__dict__)

    def add_vertex(self,node):
        self.number_of_nodes+=1
        self.adjacency_list[node]=[]

    def add_edge(self,node1,node2):
        self.adjacency_list[node1].append(node2)
        self.adjacency_list[node2].append(node1)

    def show_connections(self):
        for vertex,neighbours in self.adjacency_list.items():
            print(vertex, end='-->')
            print(' '.join(neighbours))



if __name__=='__main__':
    graph=Graph()
    graph.add_vertex('1')
    graph.add_vertex('2')
    graph.add_vertex('3')
    graph.add_vertex('4')
    graph.add_edge('1','2')
    graph.add_edge('1','3')
    graph.add_edge('1','4')
    graph.add_edge('2','3')
    graph.add_edge('2','4')
    graph.show_connections()


