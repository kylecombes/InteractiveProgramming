## Cloudy with a Chance of Ice Cream

In Cloudy with a Chance of Ice Cream, you catch falling ice cream scoops while avoiding various atmospheric obstacles. Colliding with an obstacle results in a loss of health. As you continue to ascend, the environment changes and new obstacles emerge.

This game was created for [Mini Project 4 - Interactive Programming](https://sd17spring.github.io//assignments/mini-project-4-interactive-visualization/) of Software Design at [Olin College of Engineering](http://olin.edu/).

#### To Play
Run **python3 IceCreamGame.py**. Note: the pygame library must be installed.

Link to Reflection document (also located in PDF on repo): 
/home/allison/InteractiveProgramming/Link to ReflectionSummary(1).pdf



## Initial Project Proposal

#### Minimum Viable Product

Our MVP is a game in which the player moves an ice cream cone back and forth along the x-axis using the arrow keys in an attempt to catch ice cream scoops falling vertically. Obstacles, such as asteroids, will also fall vertically, and the player will need to avoid catching the obstacles lest they sustain damage. It will have one environment, outer space, which will be represented by an appropriately themed background image.

#### Stretch Goals
We foresee our MVP being improved by implementing any of the following additions:

 * More environments ("levels"): going higher (or starting lower) in altitude would provide different background and obstacles
 * Arrow keys accelerate cone (rather than move at constant velocity)
 * Wobbling stack of scoops when cone accelerates. Player needs to be careful not to move too quickly.
 * If high level entailed flying by planets, incorporate gravity from surrounding planets and give scoops an acceleration in x-direction
 * Dynamic and adaptable difficulty thresholding

#### Individual Learning Goals

###### Allison

 * Gain more experience with the pygame library
 * Become more familiar with serious user input interactions

###### Kyle

 * Gain experience with the pygame library
 * Learn how to implement graceful environment transitions
 * Learn how to implement realistic physics simulations (gravity, ice cream scoops sensitive to toppling) in a game

## Libraries
Our game will make heavy use of the [pygame](http://pygame.org/) library.

## Timeline
By our mid-project check-in, we plan to have the following done:
* All classes defined
* Good understanding of pygame options
* Identified basic physics implementations and have idea of how to implement
* Basic user interface
* Idea of how to change the background scene
* Detailed breakdown of all the project tasks

## Predicted Roadblocks
We feel we might run into trouble with the following:
 * Implementing stretch goals and physics
 * Implementing good graphics
