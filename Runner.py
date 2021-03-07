from time import time

from Board import Board


def main():
    start = time()
    puzzle_initial = [[0, 0, 3, 0, 0, 5, 1, 0, 0],
                      [0, 0, 8, 0, 0, 0, 2, 5, 3],
                      [5, 1, 4, 7, 0, 3, 0, 0, 0],
                      [8, 6, 5, 2, 4, 9, 0, 0, 1],
                      [0, 0, 0, 1, 5, 6, 0, 0, 0],
                      [1, 0, 0, 3, 8, 7, 5, 6, 2],
                      [0, 0, 0, 5, 0, 1, 8, 3, 6],
                      [7, 5, 1, 0, 0, 0, 4, 0, 0],
                      [0, 0, 6, 4, 0, 0, 7, 0, 0]]
    board = Board(puzzle_initial)
    for i in range(100):
        board.step()
        if board.finished:
            print("Iterations: {}, Time: {}".format(i, time()-start))
            break
    print(str(board))


if __name__ == "__main__":
    main()
