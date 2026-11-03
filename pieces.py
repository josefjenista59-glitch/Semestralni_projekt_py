class Piece:
    def __init__(self, barva, row, col):
        self.barva = barva
        self.row = row
        self.col = col
        self.has_moved = False

    def moves(self, board):
        return []

class Knight(Piece):
    def moves(self, board):
        legal_moves = []
        
        mozne_posuny = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]
        
        for row, column in mozne_posuny:
            nova_row = self.row + row
            nova_col = self.col + column
            
            if 0 <= nova_row < 8 and 0 <= nova_col < 8:
                cil = board.grid[nova_row][nova_col]
                
                if cil is None or cil.barva != self.barva:
                    legal_moves.append((nova_row, nova_col))
                    
        return legal_moves

class King(Piece):
    def moves(self, board):
        legal_moves = []
        mozne_posuny = [
            (-1, -1), (-1, 0),(-1, 1),
            (0, -1), (0, 1),
            (1, -1),  (1, 0),(1, 1)
        ]
        
        for row, column in mozne_posuny:
            nova_row = self.row + row
            nova_col = self.col + column
            
            if 0 <= nova_row < 8 and 0 <= nova_col < 8:
                cil = board.grid[nova_row][nova_col]
                
                if cil is None or cil.barva != self.barva:
                    legal_moves.append((nova_row, nova_col))
                    
        return legal_moves

class Queen(Piece):
    def moves(self, board):
        legal_moves = []
        
        smery = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        for row, column in smery:
            nova_row = self.row + row
            nova_col = self.col + column
            
            while 0 <= nova_row < 8 and 0 <= nova_col < 8:
                cil = board.grid[nova_row][nova_col]
                
                if cil is None:
                    legal_moves.append((nova_row, nova_col))
                elif cil.barva != self.barva:
                    legal_moves.append((nova_row, nova_col))
                    break
                else:
                    break
                    
                nova_row += row
                nova_col += column
                
        return legal_moves

class Rook(Piece):
    def moves(self, board):
        legal_moves = []
        
        smery = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        
        for row, column in smery:
            nova_row = self.row + row
            nova_col = self.col + column
        
            while 0 <= nova_row < 8 and 0 <= nova_col < 8:
                cil = board.grid[nova_row][nova_col]
                
                if cil is None:
                    legal_moves.append((nova_row, nova_col))
                elif cil.barva != self.barva:
                    legal_moves.append((nova_row, nova_col))
                    break
                else:
                    break
                    
                nova_row += row
                nova_col += column
                
        return legal_moves

class Bishop(Piece):
    def moves(self, board):
        legal_moves = []
        
        smery = [
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        
        for row, column in smery:
            nova_row = self.row + row
            nova_col = self.col + column

            while 0 <= nova_row < 8 and 0 <= nova_col < 8:
                cil = board.grid[nova_row][nova_col]
                
                if cil is None:
                    legal_moves.append((nova_row, nova_col))
                elif cil.barva != self.barva:
                    legal_moves.append((nova_row, nova_col))
                    break
                else:
                    break
                    
                nova_row += row
                nova_col += column
                
        return legal_moves

class Pawn(Piece):
    def moves(self, board):
        legal_moves = []
        
        smer = -1 if self.barva == 'w' else 1
        
        nova_row = self.row + smer
        
        if 0 <= nova_row < 8:
            if board.grid[nova_row][self.col] is None:
                legal_moves.append((nova_row, self.col))
                
                if not self.has_moved:
                    dvojita_row = self.row + 2 * smer
                    if 0 <= dvojita_row < 8 and board.grid[dvojita_row][self.col] is None:
                        legal_moves.append((dvojita_row, self.col))
                        
            for column in [-1, 1]:
                nova_col = self.col + column
                if 0 <= nova_col < 8:
                    cil = board.grid[nova_row][nova_col]
                    if cil is not None and cil.barva != self.barva:
                        legal_moves.append((nova_row, nova_col))
                        
        return legal_moves