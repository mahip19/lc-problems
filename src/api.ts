const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5001/api'

export const getToken = (): string | null => localStorage.getItem('lc-token')
export const setToken = (token: string): void => localStorage.setItem('lc-token', token)
export const clearToken = (): void => localStorage.removeItem('lc-token')

const headers = () => ({
  'Content-Type': 'application/json',
  ...(getToken() && { Authorization: `Bearer ${getToken()}` }),
})

export const signUp = async (username: string, password: string) => {
  const res = await fetch(`${API_URL}/auth/signup`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Signup failed')
  setToken(data.token)
  return data
}

export const signIn = async (username: string, password: string) => {
  const res = await fetch(`${API_URL}/auth/signin`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Signin failed')
  setToken(data.token)
  return data
}

export const getProgress = async () => {
  const res = await fetch(`${API_URL}/user/progress`, {
    headers: headers(),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to get progress')
  return data
}

export const saveProgress = async (solvedProblems: string[]): Promise<void> => {
  const res = await fetch(`${API_URL}/user/progress`, {
    method: 'POST',
    headers: headers(),
    body: JSON.stringify({ solvedProblems }),
  })
  const data = await res.json()
  if (!res.ok) throw new Error(data.error || 'Failed to save progress')
  return data
}
