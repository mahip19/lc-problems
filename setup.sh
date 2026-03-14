#!/bin/bash

echo "🚀 LC Tracker - Setup Script"
echo "============================"
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js v16+"
    exit 1
fi

echo "✅ Node.js $(node --version) found"
echo ""

# Backend setup
echo "📦 Setting up backend..."
cd backend

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating backend/.env..."
    cat > .env << EOF
MONGODB_URI=mongodb+srv://your_user:your_password@cluster.mongodb.net/lc-tracker
JWT_SECRET=change_this_to_a_random_secret_key
PORT=5000
EOF
    echo "⚠️  Update backend/.env with your MongoDB credentials"
fi

npm install
cd ..

echo ""
echo "📦 Setting up frontend..."
npm install

echo ""
echo "✅ Setup complete!"
echo ""
echo "📖 Next steps:"
echo "1. Update backend/.env with MongoDB URI and JWT_SECRET"
echo "2. Run: npm run dev (in project root)"
echo "3. In another terminal: cd backend && npm run dev"
echo "4. Open http://localhost:5174"
