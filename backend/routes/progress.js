import express from 'express'
import User from '../models/User.js'
import { authMiddleware } from '../middleware/auth.js'

const router = express.Router()

// Get user progress
router.get('/progress', authMiddleware, async (req, res) => {
  try {
    const user = await User.findById(req.user.userId)
    if (!user) {
      return res.status(404).json({ error: 'User not found' })
    }
    res.json({ solvedProblems: user.solvedProblems })
  } catch (err) {
    console.error('Get progress error:', err)
    res.status(500).json({ error: 'Failed to get progress' })
  }
})

// Update solved problems
router.post('/progress', authMiddleware, async (req, res) => {
  try {
    const { solvedProblems } = req.body

    if (!Array.isArray(solvedProblems)) {
      return res.status(400).json({ error: 'solvedProblems must be an array' })
    }

    const user = await User.findByIdAndUpdate(
      req.user.userId,
      { solvedProblems },
      { new: true }
    )

    res.json({ solvedProblems: user.solvedProblems })
  } catch (err) {
    console.error('Update progress error:', err)
    res.status(500).json({ error: 'Failed to update progress' })
  }
})

export default router
