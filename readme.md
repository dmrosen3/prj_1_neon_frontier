Project 1 — Battle Trainer: Neon Frontier

Type: Text-based / CLI sci-fi combat simulator
Tools: Python, rich, colorama, pyfiglet, random, time, json

Concept Overview

In the year 2479, elite combat trainees plug into a neural simulation called Neon Frontier — a combat trainer AI that generates procedurally randomized arenas, environmental effects, and enemy classes.
The player enters the simulation, selects a fighter class, and battles through waves of synthetic opponents to earn credits, upgrade stats, and acquire weapons or one-use items.

Think of it as a fusion between:

Pokémon’s battle system

Slay the Spire’s upgrade loop

Fallout’s terminal aesthetic

…but built entirely in Python’s command line.

Core Gameplay Features
Category	Description
Class Selection	Choose your combat archetype: Marine (balanced), Technomancer (tech buffs), Psion (mental attacks), or Rogue Drone (speed-focused).
Procedural Arenas	Each battle occurs in a randomized environment (e.g., Solar Flare, Cryo Chamber, Nebula Field) that affects certain stats or classes.
Turn-Based Combat	Players select actions (attack, defend, use item, retreat). Combat outcomes depend on player/enemy stats, class modifiers, and RNG.
Currency & Upgrades	Defeating enemies grants credits, used to upgrade health, power, defense, or purchase consumables (stim packs, grenades, EMPs).
Progression Loop	Between rounds, players can visit a “Hub” to heal, shop, or reallocate stat points before entering the next battle tier.
🎨 Visual & Immersive Design

This project will push the limits of text-based immersion using CLI graphics.
The entire interface will be stylized as a futuristic neural simulation console:

Element	Visual Treatment
Startup Screen	pyfiglet ASCII logo, animated boot sequence using time + sys.stdout
Menus	rich.Panel and color-coded text for selection options
Battle Scenes	Dynamic HP bars using rich.Progress and colored logs for damage events
Shops & Upgrades	rich.Table layout for item and stat menus
Environmental Effects	Styled alerts like [cyan]Solar Flare active: Technomancer damage +20%![/cyan]
🧠 Key Learning Concepts

This project reinforces major Python fundamentals and applied software design:

Concept	Application
Functions & Modules	Split game logic into files (combat.py, player.py, shop.py, main.py)
OOP (Classes & Objects)	Define Player, Enemy, and Arena classes with attributes and methods
Conditionals & Loops	Turn-based logic and combat cycles
Data Persistence	Save/load player data and upgrades using JSON
Procedural Generation	Random enemy, item, and environment selection
Third-Party Libraries	Use rich, colorama, pyfiglet for CLI graphics and text effects
🧭 Stretch Features (Advanced)

Procedural enemy scaling: enemies adapt to player level or upgrades

AI behavior: enemy “personalities” that alter tactics

Status effects: bleeding, overheat, EMP paralysis, etc.

Inventory system: multiple weapon types and limited capacity

Achievements or leaderboards: stored locally via JSON or SQLite

Multiplayer hotseat mode: 2 players alternate turns