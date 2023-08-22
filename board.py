#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: David Kwon
# email: day.kwon@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if digitstr[count] == '0':
                    self.blank_r = r
                    self.blank_c = c
                self.tiles[r][c] = digitstr[count]
                count += 1

    ### Add your other method definitions below. ###
    def move_blank(self, direction):
        """ takes an input of a string direction that specifies the 
            direction in which the blank should move, and that attempts 
            to modify the contents of the called Board object accordingly.
            The method returns True or False to indicate whether the 
            requested move was possible
        """
        row = {'up': -1, 'down': 1, 'left': 0, 'right': 0} 
        col = {'up': 0, 'down': 0, 'left': -1, 'right': 1}
        if direction not in row or direction not in col:
            return False
        
        new_r = self.blank_r + row[direction]
        new_c = self.blank_c + col[direction]  
        
        if new_r < 0 or new_r > 2 or new_c < 0 or new_c > 2:
            return False
        
        self.tiles[self.blank_r][self.blank_c] = self.tiles[new_r][new_c]
        self.tiles[new_r][new_c] = '0'
        self.blank_r = new_r
        self.blank_c = new_c
        return True
    
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to 
            the current contents of the called Board object’s tiles 
            attribute
        """
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += self.tiles[r][c]      
        return s
    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy
            of the called object
        """
        copy = Board(self.digit_string())
        return copy
    
    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
            object that are not where they should be in the goal state
        """
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != '0':
                    if self.tiles[r][c] != GOAL_TILES[r][c]:
                        count += 1
        return count
    
    def placeholder(self):
        """ This heuristic compares each tile's current position and 
            finds where it should be in GOAL_TILES. Going through each 
            tile, eventually, this heuristic will determine which tile 
            will be given priority. 
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
    
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument
            (other) have the same values for the tiles attribute, and 
            False otherwise
        """
        return self.tiles == other
    
    def __repr__(self):
        """ returns a string representation of a Board object
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
    
   
               
               
               
               
               
