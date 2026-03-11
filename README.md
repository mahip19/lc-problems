# ⚡ LC Company Tracker

A powerful LeetCode problem tracker to help you prepare for technical interviews by organizing problems by company, difficulty, and topic.

## Features

- 🏢 **Company-based filtering** - View problems by company (Google, Meta, Amazon, etc.)
- 📊 **Multi-select filters** - Filter by multiple difficulties (Easy, Medium, Hard) simultaneously
- 🏷️ **Topic filtering** - Filter problems by algorithms (DFS, BFS, Two Pointers, Dynamic Programming, etc.)
- 🌙 **Dark/Light mode** - Toggle between dark and light themes
- ⭐ **Progress tracking** - Mark problems as solved and track your completion percentage
- 📈 **Sort options** - Sort by frequency or difficulty
- 💾 **Local persistence** - Your progress and theme preference are saved locally

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16 or higher) - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** (for cloning the repository)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/lc-problems.git
cd lc-problems
```

### 2. Install dependencies

```bash
npm install
```

This will install all required packages:
- Vue 3
- Vite (build tool)
- TypeScript
- Tailwind CSS

## Running Locally

### Development Server

Start the development server with hot reload:

```bash
npm run dev
```

The app will be available at: **http://localhost:5173** (or the next available port if 5173 is in use)

Your terminal will display the exact URL to use.

### Build for Production

To create an optimized build for deployment:

```bash
npm run build
```

The production-ready files will be generated in the `dist/` directory.

### Preview Production Build

To preview the production build locally:

```bash
npm run preview
```

## Project Structure

```
lc-problems/
├── src/
│   ├── App.vue           # Main application component
│   ├── main.ts           # Application entry point
│   ├── assets/
│   │   └── main.css      # Global styles
│   └── data/
│       └── problems.json # LeetCode problems database
├── public/               # Static assets
├── index.html            # HTML template
├── vite.config.ts        # Vite configuration
├── tsconfig.json         # TypeScript configuration
└── package.json          # Project dependencies
```

## Usage Guide

### Filtering Problems

1. **Select a Company** - Click the company button to choose which company's problems to view
2. **Filter by Difficulty** - Click "Difficulty" to select Easy, Medium, Hard (or any combination)
3. **Filter by Topic** - Click "Topics" to select specific algorithms or data structures
4. **Sort Results** - Choose between sorting by Frequency or Difficulty

### Tracking Progress

- Click the ⭐ icon next to a problem to mark it as solved
- Your progress is automatically saved
- View the overall completion percentage at the top

### Theme

- Click ☀️ or 🌙 to toggle between light and dark mode
- Your preference is saved automatically

### Reset Progress

- Click "Reset Progress" in the top right to clear all solved problems (confirmation required)

## Keyboard Shortcuts

- Click outside dropdowns to close them
- Use checkboxes to select multiple filter options

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Technologies Used

- **Vue 3** - Progressive JavaScript framework
- **TypeScript** - Typed JavaScript
- **Vite** - Next-generation frontend build tool
- **Tailwind CSS** - Utility-first CSS framework

## Troubleshooting

### Port already in use

If port 5173 is already in use, Vite will automatically try the next available port. Check the terminal output for the correct URL.

### Dependencies not installing

```bash
rm -rf node_modules package-lock.json
npm install
```

### App not loading

1. Clear your browser cache
2. Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
3. Check that you're on the correct URL (http://localhost:5173)

## Environment Setup

The app uses localStorage for persisting:
- Solved problems (`lc-solved`)
- Theme preference (`lc-theme`)

No environment variables are required to run locally.

## Data Source

Problem data is stored in `src/data/problems.json`. The file contains problems organized by company with the following structure:

```json
[
  {
    "company": "Google",
    "problems": [
      {
        "id": 1,
        "title": "Two Sum",
        "difficulty": "Easy",
        "frequency": 1,
        "slug": "two-sum",
        "topics": ["Array", "Hash Table"]
      }
    ]
  }
]
```

## Future Deployment

When ready to deploy:

1. Run `npm run build`
2. Deploy the `dist/` folder to your hosting platform:
   - Vercel (recommended for Vue apps)
   - Netlify
   - GitHub Pages
   - AWS S3 + CloudFront
   - Any static file hosting service

## Contributing

Feel free to add more companies, problems, or improve the UI/UX!

## License

MIT License - feel free to use this project as you wish.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

**Happy coding! 🚀 Good luck with your interviews!**
