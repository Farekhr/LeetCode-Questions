#Time complexity O(9^2), Space complexity O(9^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set) #initialize columns, rows, and boxes hashsets 
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9): #iterate through every row-column combination
            for c in range(9):
                if (board[r][c] == "."): #skip if the slot is empty
                    continue
                
                if (board[r][c] in rows[r] or #check if a given number has a duplicate in its same row, column, or box
                    board[r][c] in columns[c] or
                    board[r][c] in boxes[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c]) #add the number to its given row, box, or columns
                columns[c].add(board[r][c])
                boxes[r // 3, c // 3].add(board[r][c])
        
        return True #is valid if nothing is flagged
