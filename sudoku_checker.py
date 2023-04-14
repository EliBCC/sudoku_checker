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
        return False
    
    def getRows(self, board):
        """
        Takes a board and returns a list of rows
        :type board: List[List[str]]
        :rtype: List[List[str]]
        """
    
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
        