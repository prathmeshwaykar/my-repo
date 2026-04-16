# My Portfolio & Snake Game

A modern portfolio website featuring a responsive design and an interactive Python Snake game.

## Project Structure

```
my-repo/
├── index.html      # Main portfolio website
├── style.css       # Styling for the website
├── snake.py        # Python Snake game (Pygame)
└── README.md       # This file
```

## Files Overview

### `index.html`
The main landing page featuring:
- Modern hero section with call-to-action
- About section
- Services showcase with card layout
- Snake game information section
- Contact form
- Responsive navigation

### `style.css`
Comprehensive styling with:
- Modern color scheme and gradients
- Responsive grid layout for services
- Styled form elements
- Mobile-first responsive design
- Smooth transitions and hover effects

### `snake.py`
A playable Snake game built with Pygame featuring:
- 20x24 grid-based gameplay
- Score tracking
- Food spawning mechanics
- Collision detection (walls and self)
- Game restart functionality

## How to Use

### Viewing the Website

1. Open `index.html` in your web browser
2. Browse through the sections using the navigation menu
3. Fill out the contact form (static demo)
4. Navigate to the "Snake" section for game instructions

### Playing the Snake Game

#### Prerequisites
Install Pygame (required to run the game):
```bash
pip install pygame
```

#### Running the Game
Open a terminal in the project directory and run:
```bash
python snake.py
```

#### Game Controls
- **Arrow Keys** - Move the snake (Up, Down, Left, Right)
- **R** - Restart the game after game over

#### Game Rules
- Eat red food to grow and increase your score
- Avoid hitting walls or yourself
- Each food eaten increases your score by 1

## Features

✨ **Responsive Design** - Works on desktop, tablet, and mobile
🎮 **Interactive Game** - Fully functional Snake game with Pygame
📱 **Modern UI** - Clean, contemporary design with smooth animations
🎨 **Customizable** - Easy to modify colors, content, and layout

## Customization

### Website Content
Edit `index.html` to change:
- Title and headings
- Section content
- Contact form fields
- Navigation links

### Website Styling
Edit `style.css` to modify:
- Colors (variables at the top)
- Fonts and typography
- Layout and spacing
- Responsive breakpoints

### Game Settings
Edit `snake.py` to adjust:
- `FPS` - Game speed (default: 12)
- `CELL_SIZE` - Grid cell size (default: 20 pixels)
- Colors - RGB values for snake, food, background

## Dependencies

- **Pygame** - For the Snake game (`pip install pygame`)
- No dependencies for the website (pure HTML/CSS)

## Browser Compatibility

The website works on all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Game Compatibility

Snake.py requires Python 3.6+ and Pygame 2.0+

## Future Enhancements

- Add more game difficulty levels
- Integrate game into the website with WebGL
- Add high score tracking
- Mobile touch controls for the game
- API integration for the contact form

## License

Feel free to use and modify this project for personal and commercial purposes.

---

**Created:** April 2026
