Project 1: 2D Side-Scrolling Game Using Pygame
Team Members
Ayush Dutta
Sarita Lakai
Tirtha Raj Pokhrel
Angel Prajapati
Overview
This is a side-scrolling 2D game built using Pygame, where players control a character navigating through three levels filled with enemies, collectibles, and obstacles. The player can jump, shoot projectiles, and defeat enemies to score points. The game also features health, lives, a boss enemy at the end of each level, and a dynamic camera that follows the player’s movement.

Features
Player Class:

Movement (left, right, jump), shooting projectiles, health, and lives management.
Projectile Class:

Manages projectile speed, direction, and damage.
Enemy Class:

Enemies have movement, health, and attack patterns. Boss enemies at the end of each level.
Collectible Class:

Health boosts, extra lives, and other power-ups to aid the player.
Level Design:

Three levels with increasing difficulty, including platforming sections and a boss at the end of each level.
Scoring System:

Points based on enemies defeated and collectibles gathered.
Game Over Screen:

Displays a game over message with an option to restart the game.
Dynamic Camera:

Smoothly follows the player throughout the level.
How to Run
Install Pygame using pip install pygame.
Run the main.py file to start the game.
Use the arrow keys to move, spacebar to jump, and a designated key (e.g., “Z”) to shoot projectiles.
Game Concept
Hero: Human-like character.
Enemies: Human-like enemies and a boss at the end of each level.
Project 2: Tkinter Application Using Object-Oriented Programming (OOP) Concepts
Team Members
Ayush Dutta
Sarita Lakai
Tirtha Raj Pokhrel
Angel Prajapati
Overview
This project is a Tkinter desktop application that uses several OOP concepts, such as multiple inheritance, encapsulation, polymorphism, and method overriding. The application also integrates AI models to perform tasks such as image classification or language translation. The GUI allows users to interact with these models and display results on the application interface.

Features
OOP Concepts:
Multiple Inheritance: The application uses classes that inherit functionality from multiple parent classes.
Encapsulation: Important methods and variables are encapsulated within classes, ensuring data integrity.
Polymorphism: Common methods are overridden by different AI models to perform different tasks.
Method Overriding: Subclasses override parent class methods to achieve specific functionalities (e.g., AI model behavior).
Decorators: Python decorators are used to add functionality to class methods.
AI Models:
The application uses pre-trained models (e.g., image classification, language translation).
Input data is provided through the GUI, and the results are displayed back to the user.
How to Run
Install the required libraries: pip install tkinter (you may also need tensorflow or transformers depending on the AI model used).
Download the necessary pre-trained AI models as instructed in the project code.
Run the tkinter_app.py file to launch the desktop application.
Input data and select the AI model to process and display the output.
Examples:
Youtube-like Interface: A simple interface allowing users to upload an image or text for AI processing.
AI-based Application: Integration of AI models for tasks like object detection or translation, providing real-time output to the user.
Contributions
Ayush Dutta: Lead developer for the Pygame project and responsible for integrating the AI models in the Tkinter application.
Sarita Lakai: Assisted with game mechanics, OOP design, and UI for the Tkinter project.
Tirtha Raj Pokhrel: Worked on enemy behavior, level design, and the game-over/restart mechanism in the Pygame project.
Angel Prajapati: Responsible for scoring system, collectibles, and dynamic camera implementation in the Pygame project.
Future Improvements
Expand the Pygame project with additional levels, more complex enemy AI, and environmental obstacles.
Extend the Tkinter app with more diverse AI models and enhance user interaction options.
