# MongoDB Atlas Quick Setup

Get MongoDB running in 5 minutes for free.

## Step 1: Create Account

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register)
2. Sign up with email or Google
3. Verify email

## Step 2: Create Free Cluster

1. Click "Create" → "Build a Database"
2. Select "Free" tier (M0)
3. Choose a region (closest to you)
4. Name your cluster (e.g., "lc-tracker")
5. Click "Create Cluster"
6. Wait 1-2 minutes for cluster to deploy

## Step 3: Create Database User

1. In left sidebar, click "Database Access"
2. Click "Add New Database User"
3. Choose "Password"
4. Enter username: `lc_user`
5. Generate secure password (MongoDB suggests one) → **Copy it!**
6. Click "Add User"

## Step 4: Get Connection String

1. Go back to "Clusters" or click "Database" in sidebar
2. Click "Connect"
3. Choose "Connect your application"
4. Select "Node.js" driver
5. Copy the connection string that looks like:
```
mongodb+srv://lc_user:PASSWORD@cluster.mongodb.net/?retryWrites=true&w=majority
```

## Step 5: Configure Your App

Replace the password and database name:
```
mongodb+srv://lc_user:YOUR_PASSWORD@cluster.mongodb.net/lc-tracker
```

Create `backend/.env`:
```
MONGODB_URI=mongodb+srv://lc_user:YOUR_PASSWORD@cluster.mongodb.net/lc-tracker
JWT_SECRET=any_random_string_here_like_hello123
PORT=5000
```

## Step 6: Allow Connections (Important!)

1. Go to "Network Access" in left sidebar
2. Click "Add IP Address"
3. Select "Allow Access from Anywhere" (0.0.0.0/0)
4. Click "Confirm"

⚠️ **For development only!** In production, whitelist specific IPs.

## Step 7: Test Connection

Run backend:
```bash
cd backend
npm run dev
```

You should see:
```
Connected to MongoDB
Server running on http://localhost:5000
```

If you see connection errors, check:
- ✅ Username and password are correct
- ✅ IP whitelist includes your IP (use 0.0.0.0/0 for now)
- ✅ Database name is correct (lc-tracker)

## Free Tier Limits

- **Storage**: 512 MB (plenty for this app)
- **Database size**: 512 MB
- **Shared cluster** (no dedicated servers)
- **Perfect for**: Learning, development, small projects

## Upgrade Later

You can upgrade to paid tier anytime if you need more storage or features.
