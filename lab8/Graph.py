from networkx import draw, Graph
from pylab import show
#
g = Graph()
class Graph:
    def __init__(self):
         self.matrix_adj=[[]]
         self.matrix_incidence=[[]]
         self.list_adj={}
         self.list_arc=[]
         self.count_vert=0

    def _init_list_adj(self):
            self.list_adj={}
            for i in range(self.count_vert):
                self.list_adj.update({i:[]})
    def matr_adj_from_list_adj(self):
        self.count_vert=len(self.list_adj)
        self.matrix_adj = [[0 for j in range(0, self.count_vert)] for i in range(0, self.count_vert)]
        for i in self.list_adj:
            for j in self.list_adj[i]:
                self.matrix_adj[i][j]=1


    def matr_adj_from_lisc_arc(self):
        self.count_vert=max(self.list_arc[0])
        self.matrix_adj = [[0 for j in range(0, self.count_vert)] for i in range(0, self.count_vert)]

        for arc in self.list_arc:
            self.matrix_adj[arc[0]][arc[1]]=1
            self.matrix_adj[arc[1]][arc[0]]=1

    def matr_adj_from_matrix_incedent(self):
        self.count_vert=len(self.matrix_incidence)
        self.matrix_adj = [[0] * self.count_vert] * self.count_vert
        t=len(self.matrix_incidence[0])
        first=-1
        second=-1
        for i in range(t):
            for j in range(self.count_vert):
                if self.matrix_incidence[j][i]==1 and first==-1:
                    first=j
                elif self.matrix_incidence[j][i]==1 and second==-1:
                    second=1
                    break
            self.matrix_adj[first][second]=1
            self.matrix_adj[second][first]=1

    def list_arc_from_matr_adj(self):
        self.count_vert=len(self.matrix_adj[0])
        self.list_arc=[]
        for i in range(self.count_vert):
            for j in range(i+1,self.count_vert):
                if self.matrix_adj[i][j]>0:
                    self.list_arc.append([i,j])

    def list_arc_from_matrix_incedent(self):
        self.count_vert = len(self.matrix_incidence)
        count_arc=len(self.matrix_incidence[0])
        first = -1
        second = -1
        for i in range(count_arc):
            for j in range(self.count_vert):
                if self.matrix_incidence[j][i]==1 and first==-1:
                    first=j
                elif self.matrix_incidence[j][i]==1 and second==-1:
                    second=1
                    break
            self.list_arc.append([first,second])

    def list_arc_from_list_adj(self):
        self.count_vert = len(self.list_adj)
        self.list_arc=[]
        for i in self.list_adj:
            for j in self.list_adj[i]:
                if i<j:
                    self.list_arc.append([i,j])

    def list_adj_from_list_arc(self):
        self._init_list_adj()
        for arc in self.list_arc:
            self.list_adj.get(arc[0]).append(arc[1])
            self.list_adj.get(arc[1]).append(arc[0])

    def list_adj_from_matix_adj(self):
        self.count_vert=len(self.matrix_adj[0])
        self._init_list_adj()
        for i in range(self.count_vert):
            for j in range(self.count_vert):
                if self.matrix_adj[i][j]>0:
                    self.list_adj.get(i).append(j)

    def list_adj_from_matrix_incedent(self):
        self.count_vert = len(self.matrix_incidence)
        self._init_list_adj()
        count_arc = len(self.matrix_incidence[0])
        first = -1
        second = -1
        for i in range(count_arc):
            for j in range(self.count_vert):
                if self.matrix_incidence[j][i] == 1 and first == -1:
                    first = j
                elif self.matrix_incidence[j][i] == 1 and second == -1:
                    second = 1
                    break
            self.list_adj.get(first).append(second)
            self.list_adj.get(second).append(first)

    def matrix_incedent_from_matix_adj(self):
        self.count_vert=len(self.matrix_adj[0])
        self.list_arc_from_matr_adj()
        count_arc=len(self.list_arc)
        self.matrix_incidence = [[0 for j in range(0, count_arc)] for i in range(0, self.count_vert)]

        tmp=0
        for i in range(self.count_vert):
            for j in range(i,self.count_vert):
                if self.matrix_adj[i][j]>0:
                    print(tmp)
                    print(i)

                    self.matrix_incidence[tmp][i]=1
                    self.matrix_incidence[tmp][j]=1
            tmp+=1

    def matrix_incedent_from_list_arc(self):
        if self.count_vert==0:
            self.count_vert = max(self.list_arc[0])
        count_arc=len(self.list_arc)
        self.matrix_incidence = [[0 for j in range(0, count_arc)] for i in range(0, self.count_vert)]

        for i, arc in  enumerate(self.list_arc):
            self.matrix_incidence[arc[0]][i]=1
            self.matrix_incidence[arc[1]][i]=1

    def matrix_incedent_from_list_adj(self):
        self.list_arc_from_list_adj()
        self.matrix_incedent_from_list_arc()

    def add_vert(self):
        self.count_vert+=1
        self.list_adj.update({self.count_vert:[]})
        self.matrix_incedent_from_list_arc()
        self.list_arc_from_list_adj()
        self.matr_adj_from_list_adj()

    def del_arc(self,vert1,vert2):
        self.list_arc.remove([vert1,vert2])
        self.list_adj_from_list_arc()
        self.matr_adj_from_list_adj()
        self.matrix_incedent_from_list_arc()

    def del_vert(self,vert):
        del(self.list_adj[vert])
        self.matrix_incedent_from_list_arc()
        self.list_arc_from_list_adj()
        self.matr_adj_from_list_adj()

    def show(self):
        print("Матрица смежности")
        print(self.matrix_adj)
        print("Матрица инцидентности")
        print(self.matrix_incidence)
        print("Cписок дуг")
        print(self.list_arc)
        print("Cписок смежности")
        print(self.list_adj)
    def DFSUtil(self, v, visited):
        visited.add(v)
        for neighbour in self.list_adj[v]:
            if neighbour not in visited:
                print(str(v) +"->"+str(neighbour), end=' ')

                self.DFSUtil(neighbour, visited)
                print(str(neighbour)+'->'+str(v), end=' ')

    def DFS(self, start_vert):
        visited = set()
        self.DFSUtil(start_vert, visited)


    def add_arc(self,vert1, vert2):
                self.list_arc.append([vert1,vert2])
                self.list_adj_from_list_arc()
                self.matr_adj_from_list_adj()
                self.matrix_incedent_from_list_arc()
graph=Graph()
graph.matrix_adj=[[0,1,0,1],[0,0,1,1], [0,1,0,1],[1,0,1,0]]
graph.list_arc_from_matr_adj()
graph.list_adj_from_matix_adj()
graph.matrix_incedent_from_matix_adj()
graph.add_vert()
graph.add_arc(4,1)
graph.show()
g.add_edges_from(graph.list_arc)

print(graph.DFS(4))
draw(g, with_labels=True)
show()