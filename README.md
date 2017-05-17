# Pathfinding-in-Pacman

This repo was a short term project for CSCI 4511W (Artificial Intelligence) that uses a custom implementation of Pac-Man to compare different pathfinding algorithms. The basic Pac-Man game was written in Python 3 and utilizes non-standard libraries PIL (python imaging library) and pygame. Pathfinding algorithms are used to navigate Ghosts towards the Pac-Man sprite, where each ghost represents the use of a different search algorithm.

Installation:
  - since this program uses pygame and PIL you will need to make sure those are installed on your machine first.
  - This can be done using the pip install command:
      pip install pygame
      pip install PIL
  - Additional information on installing pygame can be found here: https://www.pygame.org/wiki/GettingStarted
  
Use:
  - Note that this game was solely created to test out different pathfinding algorithms. 
  - The overall goal was to provide evidence that incomplete real-time pathfinding algorithms can perform more efficiently and to        the same degree of accuracy as complete algorithms when tuned correctly to a finite state-space.
  - The algorithms used in the small project are Breadth First Search, A*, and Context Dependent Subgoaling A*.
  - The full project report that include results of comparing our different pathfinding algorithms can be found in the file called      "Full-Project-Report.pdf"


