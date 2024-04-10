import os
import platform
import time

print("Maze Solver. \n")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

Row = 8
Column = 8

Mat = [[0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 1, 1, 1, 1, 0],
       [0, 1, 1, 1, 0, 1, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 3, 0],
       [0, 0, 1, 1, 1, 0, 0, 0],
       [0, 1, 2, 0, 1, 1, 1, 0],
       [0, 1, 0, 0, 0, 0, 0, 0]]

Visited = [[0 for _ in range(Column)] for _ in range(Row)]
Path = [[0, 0] for _ in range(Row * Column)]
ind = 0

KeyFoundStatus = 0
ExitFoundStatus = 0

def draw_mat():
    for i in range(Row):
        for j in range(Column):
            if Mat[i][j] == 0:
                print("##", end="")
            elif Mat[i][j] == 1:
                print("  ", end="")
            elif Mat[i][j] == 2:
                print(" D", end="")
            elif Mat[i][j] == 3:
                print(" K", end="")
            else:
                print("Invalid Input. Exiting....")
                return 1
        print()

def draw_mat_with_tuples(Tuples):
    for i in range(Row):
        for j in range(Column):
            if Mat[i][j] == 0:
                print("##", end="")
            elif Mat[i][j] == 1:
                a = 0
                for k in range(len(Tuples)):
                    if Tuples[k][0] == i and Tuples[k][1] == j:
                        print(". ", end="")
                        a += 1
                        break
                if a == 0:
                    print("  ", end="")
            elif Mat[i][j] == 2:
                a = 0
                for k in range(len(Tuples)):
                    if Tuples[k][0] == i and Tuples[k][1] == j:
                        print(".D", end="")
                        a += 1
                        break
                if a == 0:
                    print(" D", end="")
            elif Mat[i][j] == 3:
                a = 0
                for k in range(len(Tuples)):
                    if Tuples[k][0] == i and Tuples[k][1] == j:
                        print(".K", end="")
                        a += 1
                        break
                if a == 0:
                    print(" K", end="")
            else:
                print("Invalid Input. Exiting....")
                return 1
        print()

def adjacent_passage_finder():
    while True:
        x, y = map(int, input("\nEnter the coordinate to check its adjacent place for passage (x y): ").split())
        print("\nThe adjacent passages of given coordinates are: ")
        if Mat[x - 1][y] == 1:
            print(f"({x - 1},{y})")
        if Mat[x + 1][y] == 1:
            print(f"({x + 1},{y})")
        if Mat[x][y - 1] == 1:
            print(f"({x},{y - 1})")
        if Mat[x][y + 1] == 1:
            print(f"({x},{y + 1})")
        choice = int(input("\nEnter 1 to find adjacent passages again and x to exit: "))
        if choice != 1:
            break

def key_to_exit(x, y):
    global ind
    if 0 <= x < Row and 0 <= y < Column and Visited[x][y] <= 1 and Mat[x][y] != 0:
        Visited[x][y] += 2
        Path[ind] = [x, y]
        ind += 1
        
        if Mat[x][y] == 2:
            print(f"\nDoor Detected at ({x},{y}).")
            draw_mat_with_tuples(Path)
            if KeyFoundStatus == 1:
                print("\nUnlocking the Door and Heading to Exit.")
            else:
                print("\nDoor can't be unlocked. Searching alternative path.")
                return False  # Door can't be unlocked
        
        if x == 0 or x == Row - 1 or y == 0 or y == Column - 1:
            print(f"\nExit Found.\nThe exit is at: ({x},{y})")
            draw_mat_with_tuples(Path)
            return True  # Exit found
        
        if (key_to_exit(x + 1, y) or 
            key_to_exit(x - 1, y) or 
            key_to_exit(x, y + 1) or 
            key_to_exit(x, y - 1)):
            return True  # Exit found
        
        ind -= 1
        Path[ind] = [0, 0]
    
    return False  # Exit not found


def to_key(x, y):
    global ind, KeyFoundStatus
    if 0 <= x < Row and 0 <= y < Column and Visited[x][y] == 0 and Mat[x][y] != 0 and Mat[x][y] != 2:
        Visited[x][y] += 1
        Path[ind] = [x, y]
        ind += 1
        
        if Mat[x][y] == 3:
            print(f"\nKey Found at ({x},{y}).")
            KeyFoundStatus += 1
            draw_mat_with_tuples(Path)
            print("\nHeading to door now.")
            key_to_exit(x, y)
        
        to_key(x + 1, y)
        to_key(x - 1, y)
        to_key(x, y + 1)
        to_key(x, y - 1)
        
        ind -= 1
        Path[ind] = [0, 0]

def main():
    global KeyFoundStatus, ExitFoundStatus, ind
    while True:
        choice = int(input("\nChoose from the options:\n1.Print the maze..\n2.Find adjacent Passages..\n3.Find the Path from entry to exit\n4.Exit the program.\n\nYour Choice: "))
        if choice == 1:
            print("\nPrint the maze in Symbolic Representation:\n\n")
            draw_mat()
            
            no_of_tuples = int(input("\nHow many tuples do you want to enter?\n"))
            Tuples = []
            print("\nEnter the tuples(x y): ")
            for _ in range(no_of_tuples):
                Tuples.append(list(map(int, input().split())))
            
            print("\nPlotting the tuples\n\n")
            draw_mat_with_tuples(Tuples)

        elif choice == 2:    
            print("\nExercise 2:\nAdjacent Passage Finder\n\n")
            draw_mat()
            adjacent_passage_finder()
        
        elif choice == 3:
            print("\nFinding Path and Plotting in Diagram\n")
            for i in range(Row):
                for j in range(Column):
                    Visited[i][j] = 0
            draw_mat()
            x, y = map(int, input("\nEnter the coordinate of Entrance (x y): ").split())
            if to_key(x, y) == 0:
                if not key_to_exit(x, y):
                    print("\nExit not found.")
                
        
        elif choice == 4:
            return
        else:
            print("Invalid Choice. Try Again.")

if __name__ == "__main__":
    main()
