# Troubleshooting Guide

## Frontend Issues

### App shows blank screen
**Cause**: Backend not running  
**Fix**: Make sure backend is running in another terminal
```bash
cd backend && npm run dev
```
Check that it says `Server running on http://localhost:5000`

### "Failed to fetch" error
**Cause**: API call failed  
**Fix**: Check browser console (F12) for error details

### "Connection refused" for localhost:5000
**Cause**: Backend not started or wrong port  
**Fix**: 
```bash
cd backend
npm run dev
# Should show: Server running on http://localhost:5000
```

### App stuck on login screen
**Cause**: Authentication failed  
**Fix**: Check browser console for errors, try signing up with new username

### "Network error" on save
**Cause**: Backend not responding  
**Fix**: Restart backend server, check it's running on port 5000

---

## Backend Issues

### "Cannot find module" errors
**Cause**: Dependencies not installed  
**Fix**: 
```bash
cd backend
npm install
npm run dev
```

### "Connected to MongoDB" never appears
**Cause**: MongoDB connection string is wrong  
**Fix**: Check `backend/.env`:
```bash
cat backend/.env
```
Verify:
- ✅ Username is correct
- ✅ Password has no special characters (or use URL encoding)
- ✅ Cluster name is correct
- ✅ Database name is `lc-tracker`

### "ECONNREFUSED" error
**Cause**: MongoDB server unreachable  
**Fix**: 
1. Verify IP whitelist in MongoDB Atlas (Network Access)
2. Use "Allow Access from Anywhere" (0.0.0.0/0) for development
3. Check your internet connection

### Server running but "Username already taken" won't clear
**Cause**: User exists in database  
**Fix**: Delete user from MongoDB Atlas or use different username

### "Invalid token" on page refresh
**Cause**: Token expired or not saved  
**Fix**: Sign in again (30-day token expiration is normal)

---

## MongoDB Issues

### Cannot connect to cluster
**Cause 1**: Wrong password  
**Fix**: Reset password in MongoDB Atlas → Database Access

**Cause 2**: IP not whitelisted  
**Fix**: Go to Network Access → Add current IP or use 0.0.0.0/0

**Cause 3**: Wrong cluster name  
**Fix**: Check connection string in MongoDB Atlas → Connect

### Cluster shows "paused"
**Cause**: Free tier auto-paused after inactivity  
**Fix**: Click cluster → Resume

### "Username not found" on signin
**Cause**: User doesn't exist in database  
**Fix**: Sign up first, then sign in

### Database storage exceeded
**Cause**: Free tier limit (512 MB)  
**Fix**: Delete old test users or upgrade to paid tier

---

## Port Issues

### Port 5000 already in use
**Check what's using it:**
```bash
lsof -i :5000  # Mac/Linux
netstat -ano | findstr :5000  # Windows
```

**Kill the process:**
```bash
kill -9 <PID>  # Mac/Linux
taskkill /PID <PID> /F  # Windows
```

**Or use different port:**
```bash
# Edit backend/.env
PORT=5001
```

### Port 5173/5174 already in use
Vite will automatically use next available port (5174, 5175, etc.)

---

## Authentication Issues

### "Username already taken" but didn't sign up
**Cause**: Someone else already used that username  
**Fix**: Choose a different username (3-20 characters)

### "Invalid username or password" on signin
**Cause**: Wrong credentials or typo  
**Fix**: 
- Check username spelling
- Usernames are **case-insensitive**
- Passwords are **case-sensitive**

### Can't remember password
**Cause**: No password reset implemented  
**Fix**: Sign up with different username

### Signed in but password changed
**Cause**: Can't change password without implementation  
**Fix**: Create new account with different username

---

## Database Issues

### How do I view my data?
**Fix**: Use MongoDB Atlas Dashboard
1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Click your cluster
3. Click "Collections" or "Browse Collections"
4. View users and documents

### How do I delete a user?
1. MongoDB Atlas → Collections → users
2. Find the user document
3. Click delete button (trash icon)

### How do I reset all data?
1. MongoDB Atlas → Collections → users
2. Click delete all (three dots → delete)
2. Confirm

---

## Performance Issues

### App is slow
**Check**:
1. Is backend running? (check terminal)
2. Is MongoDB responding? (check network tab in F12)
3. Browser has too many tabs open?

**Fix**:
- Restart backend: `npm run dev`
- Close other browser tabs
- Clear browser cache (F12 → Storage → Clear)

### Login takes 10+ seconds
**Cause**: MongoDB connecting slowly  
**Fix**: 
- Check internet connection
- Free tier may be slower, upgrade if needed

---

## Common Errors & Codes

| Error | Meaning | Fix |
|-------|---------|-----|
| `ECONNREFUSED` | Can't reach MongoDB | Check connection string & IP whitelist |
| `E11000 duplicate` | Username taken | Use different username |
| `auth/invalid-token` | Token expired/invalid | Sign in again |
| `CORS error` | Cross-origin blocked | Already allowed in Express setup |
| `MongoServerError` | Database error | Check MongoDB Atlas status |

---

## How to Debug

1. **Frontend errors**: Open browser console (F12) and look for red errors
2. **Backend errors**: Check terminal where `npm run dev` is running
3. **Database errors**: Check MongoDB Atlas logs or terminal output
4. **Network issues**: Use Network tab in DevTools (F12) to see API calls

---

## Need More Help?

Check:
- `README.md` - Setup and usage
- `MONGODB_SETUP.md` - MongoDB configuration
- `MIGRATION.md` - Technical details of changes
- Browser console (F12) for JavaScript errors
- Backend terminal for server logs
