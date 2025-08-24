import random as rand

class DSU:
    def __init__(self, sze):
        self.par = list(range(sze))
        self.rank = [1] * sze
        self.size = sze

    def find(self, vertex):
        root = vertex
        while self.par[root] != root:
            root = self.par[root]

        while vertex != root:
            temp = self.par[vertex]
            self.par[vertex] = root
            vertex = temp

        return root

    def union_(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if self.rank[root1] > self.rank[root2]:
            self.par[root2] = root1
            self.rank[root1] += self.rank[root2]
        else:
            self.par[root1] = root2
            self.rank[root2] += self.rank[root1]

    def is_connected(self, vertex1, vertex2):
        return self.find(vertex1) == self.find(vertex2)


class MazeGenerator:
    def __init__(self):
        # Co-ordinates to vertex number mapping and vice-versa
        self.dct = {}
        self.lst = []
        k = 0

        for j in range(50, 650, 30):
            for i in range(50, 650, 30):
                pt = (i + 15, j + 15)
                self.dct[pt] = k
                self.lst.append(pt)  #lst[k]= pt
                k += 1

    def generate_maze(self):
        """Generate maze and return removed walls data"""
        # Initializing DSU data structure and edge count
        d = DSU(400)
        edge_count = 0
        removed_walls = []  # Store removed walls for reconstruction

        # Do this until we obtain a spanning tree
        while edge_count < 399:
            vert = self.lst[rand.randint(0, 399)]  # randomly choosing a vertex
            nbr = (-1, -1)  # default neighbour

            if vert[0] == 65:  # left vertical line
                if vert[1] == 65:  # top-left corner
                    y_off = rand.randint(0, 1)
                elif vert[1] == 635:  # bottom-left corner
                    y_off = rand.randint(-1, 0)
                else:
                    y_off = rand.randint(-1, 1)
                if y_off == 0:
                    x_off = 1
                else:
                    x_off = 0
                nbr = (vert[0] + x_off * 30, vert[1] + y_off * 30)

            elif vert[0] == 635:  # right vertical line
                if vert[1] == 65:  # top-right corner
                    y_off = rand.randint(0, 1)
                elif vert[1] == 635:  # bottom-right corner
                    y_off = rand.randint(-1, 0)
                else:
                    y_off = rand.randint(-1, 1)
                if y_off == 0:
                    x_off = -1
                else:
                    x_off = 0
                nbr = (vert[0] + x_off * 30, vert[1] + y_off * 30)

            elif vert[1] == 65:  # top horizontal line
                x_off = rand.randint(-1, 1)  # all corner points covered, hence no need for larger if-else now onwards
                if x_off == 0:
                    y_off = 1
                else:
                    y_off = 0
                nbr = (vert[0] + x_off * 30, vert[1] + y_off * 30)

            elif vert[1] == 635:  # bottom horizontal line
                x_off = rand.randint(-1, 1)
                if x_off == 0:
                    y_off = -1
                else:
                    y_off = 0
                nbr = (vert[0] + x_off * 30, vert[1] + y_off * 30)

            else:  # all middle points
                x_off = rand.randint(-1, 1)
                if x_off == 0:
                    l = [-1, 1]
                    y_off = rand.choice(l)  # either move-up or move-down
                else:
                    y_off = 0
                nbr = (vert[0] + x_off * 30, vert[1] + y_off * 30)

            # code reached here, now decide whether to add edge or not
            vertex1 = self.dct[vert]
            vertex2 = self.dct[nbr]

            if d.is_connected(vertex1, vertex2) == False:
                d.union_(vertex1, vertex2)
                edge_count += 1
                
                # Store wall removal information
                if vert[0] == nbr[0]:  # vertical wall
                    x1 = vert[0] - 15
                    x2 = vert[0] + 15
                    y = (vert[1] + nbr[1]) / 2
                    removed_walls.append(('horizontal', (x1, y), (x2, y)))
                else:  # horizontal wall
                    x = (vert[0] + nbr[0]) / 2
                    y1 = vert[1] - 15
                    y2 = vert[1] + 15
                    removed_walls.append(('vertical', (x, y1), (x, y2)))

        return d, removed_walls
