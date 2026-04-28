# Asteroids Game (Python + Pygame)

## Overview
This project is a recreation of the classic **Asteroids** arcade game built in **Python** using the **Pygame** library. The player controls a spaceship, rotates, moves around the screen, and shoots asteroids while trying to survive.

The purpose of this project was to strengthen my understanding of **Object-Oriented Programming (OOP)** concepts such as inheritance, classes, methods, and reusable game objects.

---

## Features

- Player-controlled spaceship movement
- Rotation-based controls
- Bullet shooting system with cooldown timer
- Moving asteroids with randomized spawn patterns
- Collision detection between player, shots, and asteroids
- Asteroid splitting mechanic (large asteroids break into smaller ones)
- Game over when player collides with an asteroid
- Event logging using `game_events.jsonl`

---

## Controls

| Key | Action |
|-----|--------|
| A | Rotate Left |
| D | Rotate Right |
| W | Move Forward |
| S | Move Backward |
| Spacebar | Shoot |

---

## Technologies Used

- Python 3
- Pygame

---

## OOP Concepts Practiced

### Inheritance
Classes such as `Player`, `Asteroid`, and `Shot` inherit from a shared `CircleShape` base class.

### Encapsulation
Each object manages its own:

- position
- velocity
- drawing behavior
- update logic

### Polymorphism
Each game object overrides methods like:

- `draw()`
- `update()`

---

## Challenges I Faced and How I Solved Them

One of the biggest challenges I faced during this project was understanding how object-oriented programming works in a real application. At first, it was confusing to know when to use inheritance and how classes like `Player`, `Asteroid`, and `Shot` could all share behavior through the `CircleShape` parent class. As I continued working through the project, I began to understand how inheritance helps reduce repeated code and keeps the project organized.

Another challenge was learning how sprite groups work in Pygame. I initially struggled with why objects needed to be added to groups like `updatable` and `drawable`, but after working through it, I realized groups make it much easier to update and draw multiple game objects efficiently.

Collision detection was also difficult in the beginning. I had to understand how to calculate the distance between two objects using vectors and compare that distance to their radii. Once I broke the logic down step by step, it made much more sense.

The shooting mechanic also challenged me, especially creating a cooldown system so the player could not fire continuously. I solved this by using a timer variable that decreases over time in the update loop and only allows shooting when it reaches zero.

Overall, I learned that most programming problems become easier when broken into smaller steps and solved one piece at a time.


## What I Learned

This project helped me improve my confidence with Python and object-oriented programming. I gained hands-on experience working with game loops, collision systems, reusable classes, and real-time user input.

It also helped me understand how larger programs are organized across multiple files and classes.

---

## How to Run

1. Install pygame:

```bash
pip install pygame

2. To run the project:
    uv run main.py