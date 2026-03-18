<template>
  <div
    class="min-h-screen transition-colors duration-300 flex items-center justify-center px-4"
    :class="dark ? 'bg-[#0a0a0a] text-slate-200' : 'bg-gray-50 text-gray-800'"
  >
    <div
      class="w-full max-w-md rounded-2xl border p-8 transition-colors duration-300"
      :class="
        dark
          ? 'bg-[#111111] border-[#1a1a1a]'
          : 'bg-white border-gray-200 shadow-lg'
      "
    >
      <!-- Header -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold mb-2">⚡ LC Tracker</h1>
        <p
          class="text-sm"
          :class="dark ? 'text-slate-400' : 'text-gray-600'"
        >
          Track your LeetCode progress by company
        </p>
      </div>

      <!-- Tabs -->
      <div class="flex gap-4 mb-6">
        <button
          @click="isSignUp = false"
          class="flex-1 py-2 px-4 rounded-lg font-medium transition-colors"
          :class="
            !isSignUp
              ? dark
                ? 'bg-blue-500/20 text-blue-400'
                : 'bg-blue-100 text-blue-700'
              : dark
                ? 'text-slate-400 hover:text-slate-300'
                : 'text-gray-500 hover:text-gray-700'
          "
        >
          Sign In
        </button>
        <button
          @click="isSignUp = true"
          class="flex-1 py-2 px-4 rounded-lg font-medium transition-colors"
          :class="
            isSignUp
              ? dark
                ? 'bg-blue-500/20 text-blue-400'
                : 'bg-blue-100 text-blue-700'
              : dark
                ? 'text-slate-400 hover:text-slate-300'
                : 'text-gray-500 hover:text-gray-700'
          "
        >
          Sign Up
        </button>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleAuth">
        <!-- Username -->
        <div class="mb-4">
          <label
            class="block text-sm font-medium mb-2"
            :class="dark ? 'text-slate-300' : 'text-gray-700'"
          >
            Username
          </label>
          <input
            v-model="username"
            type="text"
            placeholder="johndoe"
            required
            minlength="3"
            maxlength="20"
            class="w-full px-4 py-2 rounded-lg border transition-colors"
            :class="
              dark
                ? 'bg-[#0a0a0a] border-[#2a2a2a] text-white focus:outline-none focus:ring-1 focus:ring-blue-500'
                : 'bg-gray-50 border-gray-300 text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-500'
            "
          />
          <p
            class="text-xs mt-1"
            :class="dark ? 'text-slate-400' : 'text-gray-500'"
          >
            3-20 characters
          </p>
        </div>

        <!-- Password -->
        <div class="mb-6">
          <label
            class="block text-sm font-medium mb-2"
            :class="dark ? 'text-slate-300' : 'text-gray-700'"
          >
            Password
          </label>
          <input
            v-model="password"
            type="password"
            placeholder="••••••••"
            required
            minlength="1"
            class="w-full px-4 py-2 rounded-lg border transition-colors"
            :class="
              dark
                ? 'bg-[#0a0a0a] border-[#2a2a2a] text-white focus:outline-none focus:ring-1 focus:ring-blue-500'
                : 'bg-gray-50 border-gray-300 text-gray-900 focus:outline-none focus:ring-1 focus:ring-blue-500'
            "
          />
        </div>

        <!-- Error Message -->
        <div
          v-if="error"
          class="mb-4 p-3 rounded-lg bg-red-500/10 text-red-400 text-sm"
        >
          {{ error }}
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="loading"
          class="w-full py-2 px-4 rounded-lg font-medium transition-colors cursor-pointer"
          :class="
            loading
              ? dark
                ? 'bg-slate-700 text-slate-400'
                : 'bg-gray-300 text-gray-500'
              : dark
                ? 'bg-blue-600 hover:bg-blue-700 text-white'
                : 'bg-blue-600 hover:bg-blue-700 text-white'
          "
        >
          {{ loading ? 'Loading...' : isSignUp ? 'Create Account' : 'Sign In' }}
        </button>
      </form>

      <!-- Footer -->
      <p class="text-center text-xs mt-6" :class="dark ? 'text-slate-500' : 'text-gray-500'">
        {{ isSignUp ? 'Already have an account?' : "Don't have an account?" }}
        <button
          @click="isSignUp = !isSignUp"
          class="text-blue-500 hover:text-blue-600 font-medium"
        >
          {{ isSignUp ? 'Sign In' : 'Sign Up' }}
        </button>
      </p>

      <!-- Theme Toggle -->
      <button
        @click="dark = !dark"
        class="absolute top-4 right-4 p-2 rounded-lg transition-colors"
        :class="
          dark
            ? 'bg-slate-800 hover:bg-slate-700 text-yellow-400'
            : 'bg-gray-200 hover:bg-gray-300 text-slate-900'
        "
      >
        {{ dark ? '☀️' : '🌙' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { signUp, signIn } from '../api'

const emit = defineEmits(['authenticated'])

const username = ref('')
const password = ref('')
const isSignUp = ref(false)
const loading = ref(false)
const error = ref('')
const dark = ref(localStorage.getItem('lc-theme') !== 'light')

async function handleAuth() {
  error.value = ''
  loading.value = true

  try {
    if (isSignUp.value) {
      await signUp(username.value, password.value)
    } else {
      await signIn(username.value, password.value)
    }
    emit('authenticated', username.value)
  } catch (err) {
    console.error('Auth error:', err.message)
    error.value = err.message || 'Authentication failed'
  } finally {
    loading.value = false
  }
}
</script>
