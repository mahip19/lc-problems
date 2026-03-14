import express from 'express'
import User from '../models/User.js'
import { generateToken } from '../middleware/auth.js'

const router = express.Router()

// Sign up
router.post('/signup', async (req, res) => {
  try {
    const { username, password } = req.body

    if (!username || !password) {
      return res.status(400).json({ error: 'Username and password required' })
    }

    // Check if user already exists
    const existingUser = await User.findOne({ username: username.toLowerCase() })
    if (existingUser) {
      return res.status(400).json({ error: 'Username already taken' })
    }

    // Create new user
    const user = new User({
      username: username.toLowerCase(),
      password,
    })

    await user.save()

    const token = generateToken(user._id, user.username)
    res.status(201).json({ token, username: user.username })
  } catch (err) {
    console.error('Signup error:', err)
    res.status(500).json({ error: 'Signup failed' })
  }
})

// Sign in
router.post('/signin', async (req, res) => {
  try {
    const { username, password } = req.body

    if (!username || !password) {
      return res.status(400).json({ error: 'Username and password required' })
    }

    // Find user
    const user = await User.findOne({ username: username.toLowerCase() })
    if (!user) {
      return res.status(401).json({ error: 'Invalid username or password' })
    }

    // Check password
    const isValidPassword = await user.comparePassword(password)
    if (!isValidPassword) {
      return res.status(401).json({ error: 'Invalid username or password' })
    }

    const token = generateToken(user._id, user.username)
    res.json({ token, username: user.username, solvedProblems: user.solvedProblems })
  } catch (err) {
    console.error('Signin error:', err)
    res.status(500).json({ error: 'Signin failed' })
  }
})

export default router
