import jwt from 'jsonwebtoken'

export const generateToken = (userId, username) => {
  const JWT_SECRET = process.env.JWT_SECRET
  if (!JWT_SECRET) {
    throw new Error('JWT_SECRET not set in environment variables')
  }
  return jwt.sign({ userId, username }, JWT_SECRET, { expiresIn: '30d' })
}

export const verifyToken = (token) => {
  try {
    const JWT_SECRET = process.env.JWT_SECRET
    if (!JWT_SECRET) {
      throw new Error('JWT_SECRET not set')
    }
    return jwt.verify(token, JWT_SECRET)
  } catch (err) {
    return null
  }
}

export const authMiddleware = (req, res, next) => {
  const token = req.headers.authorization?.replace('Bearer ', '')

  if (!token) {
    return res.status(401).json({ error: 'No token provided' })
  }

  const decoded = verifyToken(token)
  if (!decoded) {
    return res.status(401).json({ error: 'Invalid token' })
  }

  req.user = decoded
  next()
}
