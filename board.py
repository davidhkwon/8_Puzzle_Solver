#
# board.py
#
# a Board class for the Eight Puzzle
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ 
    a class for objects that represent an Eight Puzzle board
    """
    def __init__(self, digitstr):
        """ 
        constructs a Board object specified by its argument (digitstr)
        :digitstr: a permutation of the digits 0-9
        """
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1
      
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if digitstr[count] == '0':
                    self.blank_r = r
                    self.blank_c = c
                self.tiles[r][c] = digitstr[count]
                count += 1

    def __eq__(self, other):
        """ 
        compares the called object (self) and the argument (other)
        :other: Board object
        :return: True if the called object (self) and the argument (other) are identical and False otherwise
        """
        return self.tiles == other
    
    def __repr__(self):
        """ 
        constructs a printable representation of a Board object via a string
        :return: the constructed string
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s += '_ '
                else:
                    s += self.tiles[r][c] + ' '
                if c == 2:
                    s += '\n'
        return s
              
    def move_blank(self, direction):
        """ 
        verifies if the requested move is possible and modifies the Board object if so
        :direction: ['up', 'down', 'left', 'right]
        :return: True if the requested move is possible and False otherwise
        """
        r = {'up': -1, 'down': 1, 'left': 0, 'right': 0} 
        c = {'up': 0, 'down': 0, 'left': -1, 'right': 1}
        if direction not in r or direction not in c:
            return False
        
        new_r = self.blank_r + r[direction]
        new_c = self.blank_c + c[direction]  
        
        if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
            return False
        
        self.tiles[self.blank_r][self.blank_c] = self.tiles[new_r][new_c]
        self.tiles[new_r][new_c] = '0'
        self.blank_r = new_r
        self.blank_c = new_c
        return True
    
    def digit_string(self):
        """
        construct a string of digits that corresponds to the current state of the Board object
        :return: the constructed string
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += self.tiles[r][c]      
        return s
    
    def copy(self):
        """
        constructs a deep copy of the Board object
        :return: the constructed deep copy
        """
        copy = Board(self.digit_string())
        return copy
    
    def num_misplaced(self):
        """ 
        counts the number of tiles in the Board object that are misplaced
        :return: the count
        """
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != '0':
                    if self.tiles[r][c] != GOAL_TILES[r][c]:
                        count += 1
        return count
    
    def placeholder(self):
        """
        finds which tile will be given priority by comparing each tile's current position to its goal position
        :return: the priority tile
        """
        priority = 0
        for row in range(len(self.tiles)):
           for col in range(len(self.tiles[0])):
               tile = self.tiles[row][col]
               if tile != GOAL_TILES[row][col]:
                   priority += abs(row - int(tile) // 3)
                   priority += abs(col - int(tile) % 3)
               else:
                   None
                 
        return priority
