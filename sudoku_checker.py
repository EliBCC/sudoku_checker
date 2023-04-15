# https://leetcode.com/problems/valid-sudoku/
"""
Strategy:
First break down board into regions
Regions may be rows, columns, or sub-boxes
Next, check if each region is valid
If all regions are valid, board is valid
"""
class Solution(object):

    def isValidRegion(self, region):
        """
        Takes a region and checks if it is valid
        :type region: List[str]
        :rtype: bool
        """
        region = [num for num in region if num != '.']
        unique_region = set(region)
        if(len(region) != len(unique_region)):
            return False
        
        for num in region:
            if not 0 < int(num) < 10:
                return False

        return True
    
    def getRows(self, board):
        """
        Takes a board and returns a list of rows
        :type board: List[List[str]]
        :rtype: List[List[str]]
        """

        return board
    
    def getCols(self, board):
        """
        Takes a board and returns a list of columns
        :type board: List[List[str]]
        :rtype: List[List[str]]
        """
    
    def getSubBoxes(self, board):
        """
        Takes a board and returns a list of columns
        :type board: List[List[str]]
        :rtype: List[List[str]]
        """

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
