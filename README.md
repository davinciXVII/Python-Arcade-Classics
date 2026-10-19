# 🕹️ Python Arcade Classics Collection

Welcome to the **Python Arcade Classics Collection**! This repository is a curated archive of 10 recreated retro engines, platformers, and tactical arcade clones inspired by the legendary NES (Dandy), Sega, and classic desktop browser hits. 

Every project in this collection focuses on recreating complex 2D game loops, mechanical state handling, custom physics simulations, and advanced coordinate interaction layouts utilizing Python.

---

## 🎮 The Arcade Showcase

| Game Title | Mechanics Implemented | Core Tech Highlight |
| :--- | :--- | :--- |
| **Bomberman Arcade** | Grid-based bomb ticking, tactical explosion propagation, pathfinding logic, and block destruction arrays. | Object interaction matrices |
| **Contra: Python Edition** | Side-scrolling platform physics, directional bullet vectors, variable jumping curves, and sprite hitbox scaling. | Multi-layered 2D collision tracking |
| **Battle City Tanks** | Fixed-grid tactical combat, obstacle destruction layers (brick/steel), directional shell movement, and enemy respawn loops. | Complex spatial grid coordinate handling |
| **Plants vs Zombies Mini** | Lane-based tower defense loops, sunlight economy management arrays, progressive wave spawning timers, and attack projectiles intersection. | Asynchronous state loop simulation |
| **Star Wars: Space Shooter**| Vertical scrolling space arcade, procedural wave spawning, laser projectile destruction grids, and real-time score scaling. | Dynamic entity array management |
| **Chrome Dino Runner** | Endless scrolling backgrounds, progressive game-speed scaling, randomized obstacle generation, and duck/jump collision vectors. | Linear frame-rate delta speed adjustments |
| **Flappy Bird Retro** | Velocity-based gravity vector simulation, dynamic pipe obstacle rendering, tight boundary collision checking, and high-score saving logic. | Simulated physics acceleration models |
| **Retro Racing Simulator** | Top-down micro-racing, drift boundary checking, fluid acceleration/deceleration coefficients, and track intersection tracking. | Vector reflection properties |
| **Pong Classic** | 2D sports layout, paddle deflection angle calculations, responsive AI paddle tracking logs, and screen-edge bounce logic. | Real-time coordinate translation |
| **Cheat Code Engine** | Live keyboard inputs caching, string buffer matching logic, and runtime game state modification systems. | Real-time sequence validation arrays |

---

## 🛠️ Architecture & Concepts Applied

By developing these engines from scratch, I applied and mastered several advanced software engineering principles essential for a junior developer:
- **State-Machine Architecture:** Managing game states (Main Menu, Gameplay, Pause, Game Over) cleanly.
- **Complex Collision Matrices:** Implementing precise object intersection rules (bounding boxes/hitboxes) without high framework overhead.
- **Dynamic Resource Handling:** Managing spawning arrays, recycling arrays for projectiles, and tracking active entity coordinates efficiently.
- **Logic Isolation:** Ensuring game loops compute math independently from rendering layers to keep frame-rates consistent.

---

## 💻 Setup and Play

1. Clone this repository to your local machine:
```bash
git clone https://github.com
```
2. Navigate to any specific game directory:
```bash
cd plants-vs-zombies-mini
```
3. Run the primary game execution script (e.g., `main.py` or the specific module file):
```bash
python main.py
```


