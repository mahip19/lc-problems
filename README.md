# ⚡ LC Tracker

A simple LeetCode problem tracker with username/password authentication and MongoDB backend.

## Features

✅ **Username + Password auth** - No email needed  
✅ **Cloud sync** - Progress saved to MongoDB  
✅ **Company filtering** - Google, Meta, Amazon, etc.  
✅ **Multi-select filters** - Filter by difficulty and topics  
✅ **Progress tracking** - Mark solved problems and see completion %  
✅ **Dark/Light mode** - Toggle themes  
✅ **Simple backend** - REST API with JWT tokens

## Prerequisites

- Node.js (v16+)
- MongoDB Atlas account (free)

## Quick Start

### 1. Set up MongoDB Atlas

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Create database user with password
4. Get connection string: `mongodb+srv://username:password@cluster.mongodb.net/lc-tracker`

### 2. Backend Setup

```bash
cd backend
npm install
```

Create `backend/.env`:
```
MONGODB_URI=mongodb+srv://your_user:your_password@cluster.mongodb.net/lc-tracker
JWT_SECRET=your_secret_key_here
PORT=5000
```

Start backend:
```bash
npm run dev
```

Should show: `Server running on http://localhost:5000`

### 3. Frontend Setup

```bash
npm install
npm run dev
```

Open http://localhost:5174

## How to Use

1. **Sign Up** - Enter username (3-20 chars) and password, click "Create Account"
2. **Sign In** - Use your username and password
3. **Track** - Click checkboxes to mark problems as solved
4. **Filter** - Use dropdowns for difficulty and topics
5. **Sync** - Progress auto-saves to MongoDB

## API Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/signup` | Create account |
| POST | `/api/auth/signin` | Login |
| GET | `/api/user/progress` | Get solved problems |
| POST | `/api/user/progress` | Save solved problems |

All user endpoints require `Authorization: Bearer <token>` header

## Project Structure

```
lc-problems/
├── backend/
│   ├── models/User.js
│   ├── middleware/auth.js
│   ├── routes/auth.js
│   ├── routes/progress.js
│   ├── server.js
│   └── .env
├── src/
│   ├── components/AuthForm.vue
│   ├── App.vue
│   ├── api.ts
│   └── data/problems.json
└── package.json
```


## Troubleshooting

**"Connection refused" on localhost:5000**
- Ensure backend is running: `cd backend && npm run dev`

**"Username already taken"**
- Choose a different username

**MongoDB connection error**
- Verify `MONGODB_URI` in `backend/.env`
- Whitelist your IP in MongoDB Atlas (0.0.0.0/0 for development)

## Build for Production

```bash
npm run build       # Frontend
cd backend && npm install  # Backend dependencies
```

Deploy frontend to Vercel/Netlify and backend to Heroku/Railway.

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
