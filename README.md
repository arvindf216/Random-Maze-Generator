UPDATE: Code has been modified to output mazes constructed out of a 40x40 grid to obtain mazes of higher difficulty.

Random Maze Generator

- Python code to create a random maze out of a 20x20 grid
- Utilized Python library Pygame for graphical rendering
- Implemented Disjoint Set Union Data structure to keep track of the connectivity of the connected component by labelling the sets of cells as vertices
- Implemented a Kruskal-like algorithm to build a minimum spanning tree out of the cells, resulting in diverse and challenging mazes


Here are a few mazes obtained using the code:

<img src="https://github.com/arvindf216/Random-Maze-Generator/assets/138092643/d355424c-36d4-440b-8649-53e58f22c009" width="300" height="300">

<img src="https://github.com/arvindf216/Random-Maze-Generator/assets/138092643/df2c803a-dc8c-4412-813f-2f3aff811a50" width="300" height="300">

<img src="https://github.com/arvindf216/Random-Maze-Generator/assets/138092643/b2a7a5fe-6d84-49d3-9939-fb157e68e341" width="300" height="300">

<img src="https://github.com/arvindf216/Random-Maze-Generator/assets/138092643/aa664542-e7a5-43d3-b3fa-9dafdb29849c" width="300" height="300">


Scope for future development: To create a tool that will assist in navigating the maze by guiding a snake from the entry point to the destination using mouse clicks. Additionally, I want to create a maze solver that can work through mazes of any size or complexity.
