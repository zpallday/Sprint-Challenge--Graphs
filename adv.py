from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

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




def the_world(world, traversal_path):
    q = Queue()
    visited = set()
    q.enqueue([player.current_room.id])
    while q.size() > 0:
        path = q.dequeue()
        last_room = path[-1]
        if last_room not in visited:
            visited.add[last_room]
        for neighbor in graph[last_room]:
            if graph[last_room][exit] == '?':
                return path
            else:
                path_copy = list(path)
                path_copy = append[last_room][neighbor]
                q.enqueue = (path_copy)
    return True



def the_moves(world, m_moves):
    current_end = graph[player.current_room.id]
    tried = []
    for direction in current_end:
        if current_end[direction] == '?':
            tried.append(direction)
        if len(tried) == 0:
            non_explore = explore(player, m_moves)
            room_number = player.current_room.id
            for v in graph[room_number]:
                if graph[room_number][v] == next:
                    m_moves.enqueue(v)
                    room_number = next
    else:
        m_move.enqueue(tried.exit[random.randint(0)])
        len(tired_end [- 1])


# compass = {'n,e,w,s'}



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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
