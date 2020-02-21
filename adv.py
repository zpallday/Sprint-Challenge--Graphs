from room import Room
from player import Player
from world import World
import random
from ast import literal_eval
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"
# map_file = "maps/custom.txt"
# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []





def the_world(player, traversal_path):
    # init queue
    q = Queue()
    # init set for visited rooms
    visited = set()
    # add current room to queue
    q.enqueue([player.current_room.id])
    # if queue is bigger than 0 there are things to explore
    while q.size() > 0:
        path = q.dequeue()
        # keep track of last room visited
        last_room = path[-1]
        if last_room not in visited:
            # add to list of visited
            visited.add(last_room)
            #  finding an exit in the room that's unexplored
            for exit in graph[last_room]:
                 # if exot has been explored
                if graph[last_room][exit] == "?":
                    return path
                    # removing path as already explored
                else:
                    path_copy = list(path)
                    path_copy.append(graph[last_room][exit])
                    q.enqueue(path_copy)
    return []





def the_moves(player, m_moves):
    # end with current room
    current_end = graph[player.current_room.id]
    untried_end = []

    for direction in current_end:
         # if explored
        if current_end[direction] == "?":
            untried_end.append(direction)
    if len(untried_end) == 0:
        unexplored = the_world(player, m_moves)
        # room number in player current room
        room_number = player.current_room.id
        for next in unexplored:
            # 
            for direction in graph[room_number]:
                if graph[room_number][direction] == next:
                    m_moves.enqueue(direction)
                    room_number = next
                    break
    else:
        m_moves.enqueue(untried_end[random.randint(0, len(untried_end) - 1)])
#  how many chances



chances = 1
# best path
optimum_len = 500
optimum_path = []
# loop for how many times
for x in range(chances):
    player = Player(world.starting_room)
    graph = {}
    another_room = {}
    # dir in the curr room exit
    for direction in player.current_room.get_exits():
        # if explored
        another_room[direction] = "?"
    graph[world.starting_room.id] = another_room
    m_moves = Queue()
    total_moves = []
    the_moves(player, m_moves)

    compass = {"n": "s", "s": "n", "e": "w", "w": "e"}

    while m_moves.size() > 0:
        # starting is player curr room with id
        starting = player.current_room.id
        # dequeue next move
        next = m_moves.dequeue()
        player.travel(next)

        total_moves.append(next)
        end = player.current_room.id
        graph[starting][next] = end
        if end not in graph:
            graph[end] = {}
            for exit in player.current_room.get_exits():
                graph[end][exit] = "?"
        graph[end][compass[next]] = starting
        if m_moves.size() == 0:
            the_moves(player, m_moves)
        if len(total_moves) < optimum_len:
            optimum_path = total_moves
            optimum_len = len(total_moves)

traversal_path = optimum_path


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
