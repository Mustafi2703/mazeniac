# Maze Solver Project

A Python implementation of a maze generator and solver using depth-first search (DFS) algorithm with visual representation.

## Overview

This project creates random mazes and solves them using the DFS algorithm. The maze is represented as a grid of cells, where each cell has walls that can be removed to create passages.

## Features

- Random maze generation
- DFS-based maze solving
- Visual representation of maze and solution path
- Unit tests for maze logic

## How It Works

### Maze Generation

The maze is generated using a grid of cells. Each cell has four walls (top, right, bottom, left), and the generation algorithm works by:
1. Starting from a random cell
2. Randomly breaking walls between adjacent cells
3. Continuing until all cells are visited

### Depth-First Search (DFS) Algorithm

The DFS maze solving algorithm works as follows:
1. Starting from the entrance cell, mark it as visited
2. For each adjacent cell that hasn't been visited and is accessible (no wall between):
   - Move to that cell
   - Recursively apply the same process
   - If a dead-end is reached, backtrack
3. Continue until the exit is found or all possibilities are exhausted

DFS uses a stack-based approach (utilizing the call stack through recursion) to remember the path, exploring as far as possible along each branch before backtracking.

### Implementation Details

- The `Cell` class represents individual cells in the maze with their walls
- The `Maze` class manages the collection of cells and implements the algorithms
- The solution path is visually distinguished from the explored paths

## Running the Project

## Run the maze generator and solver
python maze.py

## Run the tests
python tests.py

Install requirements from requirements.txt.

## License
A personal project for educational purposes. 
