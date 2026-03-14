# Migration from Firebase to MongoDB + Express Backend

## Summary of Changes

Removed all Firebase dependencies and replaced with a simple Node.js/Express backend connected to MongoDB.

### Removed Files
- `src/firebase.ts` - Firebase initialization
- `.env.example` (old Firebase config) - Replaced with `backend/.env.example`
- `.env.local` - Firebase environment variables

### New Files Created

#### Backend Structure (`/backend`)
- `server.js` - Express server entry point
- `models/User.js` - MongoDB user schema with password hashing
- `middleware/auth.js` - JWT token generation and verification
- `routes/auth.js` - Signup/signin endpoints
- `routes/progress.js` - Progress sync endpoints
- `package.json` - Backend dependencies
- `.env` - MongoDB URI and JWT secret
- `.env.example` - Template for environment variables

#### Frontend Updates
- `src/api.ts` - Replaced Firebase imports with REST API client
  - `signUp(username, password)` - Sign up with backend
  - `signIn(username, password)` - Sign in with backend
  - `getProgress()` - Fetch solved problems from backend
  - `saveProgress(solvedProblems)` - Save to backend
  - JWT token management (localStorage)

- `src/components/AuthForm.vue` - Removed Firebase auth SDK
  - Now uses simple REST API calls
  - No email required, just username + password
  - Cleaner error handling

- `src/App.vue` - Complete Firebase removal
  - Removed `onAuthStateChanged` and `signOut`
  - Removed Firebase database calls
  - Updated to use `getProgress()` and `saveProgress()`
  - Token-based authentication via API

### How It Works

1. **Sign Up** → POST `/api/auth/signup` → Backend stores hashed password in MongoDB → Returns JWT token
2. **Sign In** → POST `/api/auth/signin` → Backend verifies password → Returns JWT token
3. **Save Progress** → POST `/api/user/progress` with JWT token → Backend updates MongoDB
4. **Load Progress** → GET `/api/user/progress` with JWT token → Backend retrieves from MongoDB

### Dependencies Removed
- `firebase@^12.10.0`

### Dependencies Added (Backend)
- `express` - Web framework
- `mongoose` - MongoDB ODM
- `bcryptjs` - Password hashing
- `jsonwebtoken` - JWT tokens
- `cors` - Cross-origin requests
- `dotenv` - Environment variables

### Running the Application

#### Terminal 1: Backend
```bash
cd backend
npm install
npm run dev
# Server runs on http://localhost:5000
```

#### Terminal 2: Frontend
```bash
npm install
npm run dev
# App opens on http://localhost:5174
```

### Key Differences

| Firebase | MongoDB + Express |
|----------|-------------------|
| Cloud-hosted | Self-hosted backend |
| Email required | Username only |
| Firebase dashboard | MongoDB Atlas dashboard |
| Real-time database | REST API |
| Google-managed | Custom API |
| No backend code | Full control of backend |

### Database Schema

```javascript
User {
  username: String (unique, lowercase, 3-20 chars)
  password: String (hashed with bcrypt)
  solvedProblems: [String] (array of problem IDs)
  createdAt: Date
  updatedAt: Date
}
```

### Environment Setup

**Backend (.env)**
```
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/lc-tracker
JWT_SECRET=random_secret_key
PORT=5000
```

**Frontend** - No environment file needed (API URL hardcoded to localhost:5000)

### Next Steps for Deployment

1. **Backend**: Deploy to Heroku, Railway, or similar Node.js host
2. **Database**: Create MongoDB Atlas cluster (free tier available)
3. **Frontend**: Deploy to Vercel/Netlify
4. Update `src/api.ts` `API_URL` to production backend
5. Set `JWT_SECRET` to a random secure string in production

### Testing

1. Sign up with username "testuser" and password "123"
2. Sign in with same credentials
3. Mark some problems as solved
4. Refresh page - progress should persist
5. Sign in from different browser/device - progress syncs

