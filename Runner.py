from time import time

from Board import Board


def main():
    start = time()
    puzzle_initial = [[0, 0, 0, 4, 0, 7, 0, 3, 0],
                      [8, 0, 0, 0, 0, 0, 2, 0, 0],
                      [0, 0, 4, 0, 0, 1, 8, 0, 0],
                      [0, 0, 0, 0, 7, 0, 0, 1, 2],
                      [0, 9, 0, 0, 0, 0, 0, 6, 0],
                      [4, 2, 0, 0, 3, 0, 0, 0, 0],
                      [0, 0, 3, 5, 0, 0, 4, 0, 0],
                      [0, 0, 8, 0, 0, 0, 0, 0, 1],
                      [0, 1, 0, 6, 0, 9, 0, 0, 0]]
    board = Board(puzzle_initial)
    for i in range(1000):
        board.step()
        if board.finished:
            print("Iterations: {}, Time: {}".format(i, time()-start))
            break
    print(str(board))


if __name__ == "__main__":
    main()
