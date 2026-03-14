<template>
  <!-- Show auth form if not logged in -->
  <AuthForm v-if="!user" @authenticated="handleAuthenticated" />

  <!-- Show app if logged in -->
  <div v-else class="min-h-screen transition-colors duration-300" :class="dark ? 'bg-[#0a0a0a] text-slate-200' : 'bg-gray-50 text-gray-800'">
    <!-- Header -->
    <header
      class="sticky top-0 z-10 border-b transition-colors duration-300"
      :class="
        dark
          ? 'border-[#1a1a1a] bg-[#111111]'
          : 'border-gray-200 bg-white shadow-sm'
      "
    >
      <div class="max-w-5xl mx-auto px-4 py-4" @click="openDropdown = null">
        <div class="flex items-center justify-between mb-3">
          <h1
            class="text-lg font-bold tracking-tight"
            :class="dark ? 'text-white' : 'text-gray-900'"
          >
            ⚡ LC Company Tracker
          </h1>
          <div class="flex items-center gap-2">
            <span class="text-xs px-2 py-1 rounded" :class="dark ? 'text-slate-500' : 'text-gray-600'">
              {{ username }}
            </span>
            <button
              @click="toggleTheme"
              class="text-xs cursor-pointer px-2 py-1 rounded transition-colors"
              :class="
                dark
                  ? 'text-slate-400 hover:text-yellow-400 hover:bg-yellow-500/10'
                  : 'text-slate-500 hover:text-indigo-500 hover:bg-indigo-500/10'
              "
            >
              {{ dark ? "☀️ Light" : "🌙 Dark" }}
            </button>
            <button
              @click="showResetConfirm = true"
              class="text-xs cursor-pointer px-2 py-1 rounded transition-colors"
              :class="
                dark
                  ? 'text-slate-500 hover:text-red-400 hover:bg-red-500/10'
                  : 'text-slate-400 hover:text-red-500 hover:bg-red-500/10'
              "
            >
              Reset Progress
            </button>
            <button
              @click="handleLogout"
              class="text-xs cursor-pointer px-3 py-1 rounded font-medium transition-colors"
              :class="
                dark
                  ? 'text-slate-500 hover:text-red-400 hover:bg-red-500/10'
                  : 'text-slate-400 hover:text-red-500 hover:bg-red-500/10'
              "
            >
              Logout
            </button>
          </div>
        </div>

        <div class="flex flex-wrap gap-2 items-center">
          <!-- Company Filter -->
          <div class="relative" @click.stop>
            <button
              @click.stop="
                openDropdown = openDropdown === 'company' ? null : 'company'
              "
              class="rounded-full px-3 py-1.5 text-sm font-medium transition-colors cursor-pointer flex items-center gap-1"
              :class="
                dark
                  ? 'bg-blue-500/20 text-blue-400 hover:bg-blue-500/30'
                  : 'bg-blue-100 text-blue-700 hover:bg-blue-200'
              "
            >
              {{ selectedCompany }}
              <svg
                class="w-4 h-4 transition-transform"
                :class="openDropdown === 'company' ? 'rotate-180' : ''"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                ></path>
              </svg>
            </button>
            <div
              v-if="openDropdown === 'company'"
              class="absolute left-0 mt-1 rounded-lg shadow-lg border min-w-max z-20"
              :class="
                dark
                  ? 'bg-[#1a1a1a] border-[#2a2a2a]'
                  : 'bg-white border-gray-200'
              "
            >
              <div
                v-for="c in companyNames"
                :key="c"
                @click.stop="
                  selectedCompany = c;
                  openDropdown = null;
                "
                class="px-4 py-2 cursor-pointer text-sm hover:bg-emerald-500/20"
                :class="
                  selectedCompany === c
                    ? 'font-bold text-emerald-400'
                    : dark
                      ? 'text-slate-300'
                      : 'text-gray-700'
                "
              >
                {{ c }}
              </div>
            </div>
          </div>

          <!-- Difficulty Filters -->
          <div class="relative" @click.stop>
            <button
              @click.stop="
                openDropdown =
                  openDropdown === 'difficulty' ? null : 'difficulty'
              "
              class="rounded-full px-3 py-1.5 text-sm font-medium transition-colors cursor-pointer flex items-center gap-1"
              :class="
                selectedDifficulties.size === 0
                  ? dark
                    ? 'bg-slate-700/50 text-slate-400 hover:bg-slate-700/70'
                    : 'bg-gray-200 text-gray-600 hover:bg-gray-300'
                  : dark
                    ? 'bg-purple-500/20 text-purple-400 hover:bg-purple-500/30'
                    : 'bg-purple-100 text-purple-700 hover:bg-purple-200'
              "
            >
              <span v-if="selectedDifficulties.size === 0">Difficulty</span>
              <span v-else class="flex items-center gap-1">
                {{ Array.from(selectedDifficulties).join(", ") }}
                <button
                  @click.stop="
                    selectedDifficulties = new Set();
                    openDropdown = null;
                  "
                  class="text-lg leading-none hover:scale-125"
                >
                  ×
                </button>
              </span>
              <svg
                v-if="selectedDifficulties.size === 0"
                class="w-4 h-4 transition-transform"
                :class="openDropdown === 'difficulty' ? 'rotate-180' : ''"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                ></path>
              </svg>
            </button>
            <div
              v-if="openDropdown === 'difficulty'"
              class="absolute left-0 mt-1 rounded-lg shadow-lg border min-w-max z-20"
              :class="
                dark
                  ? 'bg-[#1a1a1a] border-[#2a2a2a]'
                  : 'bg-white border-gray-200'
              "
            >
              <div
                v-for="d in ['Easy', 'Medium', 'Hard']"
                :key="d"
                @click.stop="toggleDifficulty(d)"
                class="px-4 py-2 cursor-pointer text-sm hover:bg-purple-500/20 flex items-center gap-2"
                :class="dark ? 'text-slate-300' : 'text-gray-700'"
              >
                <input
                  type="checkbox"
                  :checked="selectedDifficulties.has(d)"
                  class="cursor-pointer"
                />
                {{ d }}
              </div>
            </div>
          </div>

          <!-- Topic Filters -->
          <div class="relative" @click.stop>
            <button
              @click.stop="
                openDropdown = openDropdown === 'topic' ? null : 'topic'
              "
              class="rounded-full px-3 py-1.5 text-sm font-medium transition-colors cursor-pointer flex items-center gap-1"
              :class="
                selectedTopics.size === 0
                  ? dark
                    ? 'bg-slate-700/50 text-slate-400 hover:bg-slate-700/70'
                    : 'bg-gray-200 text-gray-600 hover:bg-gray-300'
                  : dark
                    ? 'bg-pink-500/20 text-pink-400 hover:bg-pink-500/30'
                    : 'bg-pink-100 text-pink-700 hover:bg-pink-200'
              "
            >
              <span v-if="selectedTopics.size === 0">Topics</span>
              <span
                v-else
                class="flex items-center gap-1 max-w-xs overflow-hidden text-ellipsis whitespace-nowrap"
              >
                {{ Array.from(selectedTopics).slice(0, 2).join(", ")
                }}{{ selectedTopics.size > 2 ? "..." : "" }}
                <button
                  @click.stop="
                    selectedTopics = new Set();
                    openDropdown = null;
                  "
                  class="text-lg leading-none hover:scale-125 flex-shrink-0"
                >
                  ×
                </button>
              </span>
              <svg
                v-if="selectedTopics.size === 0"
                class="w-4 h-4 transition-transform"
                :class="openDropdown === 'topic' ? 'rotate-180' : ''"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                ></path>
              </svg>
            </button>
            <div
              v-if="openDropdown === 'topic'"
              class="absolute left-0 mt-1 rounded-lg shadow-lg border min-w-max z-20 max-h-64 overflow-y-auto"
              :class="
                dark
                  ? 'bg-[#1a1a1a] border-[#2a2a2a]'
                  : 'bg-white border-gray-200'
              "
            >
              <div
                v-for="t in topicsList"
                :key="t"
                @click.stop="toggleTopic(t)"
                class="px-4 py-2 cursor-pointer text-sm hover:bg-pink-500/20 flex items-center gap-2"
                :class="dark ? 'text-slate-300' : 'text-gray-700'"
              >
                <input
                  type="checkbox"
                  :checked="selectedTopics.has(t)"
                  class="cursor-pointer"
                />
                {{ t }}
              </div>
            </div>
          </div>

          <!-- Sort -->
          <div class="relative ml-auto" @click.stop>
            <button
              @click.stop="
                openDropdown = openDropdown === 'sort' ? null : 'sort'
              "
              class="rounded-full px-3 py-1.5 text-sm font-medium transition-colors cursor-pointer flex items-center gap-1"
              :class="
                dark
                  ? 'bg-slate-700/50 text-slate-400 hover:bg-slate-700/70'
                  : 'bg-gray-200 text-gray-600 hover:bg-gray-300'
              "
            >
              Sort: {{ sortBy === "frequency" ? "Frequency" : "Difficulty" }}
              <svg
                class="w-4 h-4 transition-transform"
                :class="openDropdown === 'sort' ? 'rotate-180' : ''"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                ></path>
              </svg>
            </button>
            <div
              v-if="openDropdown === 'sort'"
              class="absolute right-0 mt-1 rounded-lg shadow-lg border min-w-max z-20"
              :class="
                dark
                  ? 'bg-[#1a1a1a] border-[#2a2a2a]'
                  : 'bg-white border-gray-200'
              "
            >
              <div
                @click="
                  sortBy = 'frequency';
                  openDropdown = null;
                "
                class="px-4 py-2 cursor-pointer text-sm hover:bg-slate-500/20"
                :class="
                  sortBy === 'frequency'
                    ? 'font-bold text-emerald-400'
                    : dark
                      ? 'text-slate-300'
                      : 'text-gray-700'
                "
              >
                Frequency
              </div>
              <div
                @click.stop="
                  sortBy = 'difficulty';
                  openDropdown = null;
                "
                class="px-4 py-2 cursor-pointer text-sm hover:bg-slate-500/20"
                :class="
                  sortBy === 'difficulty'
                    ? 'font-bold text-emerald-400'
                    : dark
                      ? 'text-slate-300'
                      : 'text-gray-700'
                "
              >
                Difficulty
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>

    <!-- Reset modal -->
    <div
      v-if="showResetConfirm"
      class="fixed inset-0 bg-black/60 flex items-center justify-center z-50"
      @click.self="showResetConfirm = false"
    >
      <div
        class="rounded-2xl p-6 border max-w-sm mx-4 text-center"
        :class="
          dark
            ? 'bg-[#161616] border-[#2a2a2a]'
            : 'bg-white border-gray-200 shadow-xl'
        "
      >
        <div class="text-4xl mb-3">🗑️</div>
        <h3
          class="text-lg font-bold mb-2"
          :class="dark ? 'text-white' : 'text-gray-900'"
        >
          Reset all progress?
        </h3>
        <p
          class="text-sm mb-5"
          :class="dark ? 'text-slate-400' : 'text-gray-500'"
        >
          This will uncheck all {{ solvedCountGlobal }} solved problems across
          every company. Can't undo this.
        </p>
        <div class="flex gap-3">
          <button
            @click="showResetConfirm = false"
            class="flex-1 px-4 py-2.5 rounded-xl bg-slate-700 text-white text-sm font-medium hover:bg-slate-600 transition-colors cursor-pointer"
          >
            Nah, keep it
          </button>
          <button
            @click="resetProgress"
            class="flex-1 px-4 py-2.5 rounded-xl bg-red-500 text-white text-sm font-medium hover:bg-red-600 transition-colors cursor-pointer"
          >
            Nuke it 💥
          </button>
        </div>
      </div>
    </div>

    <main class="max-w-5xl mx-auto px-4 py-5">
      <!-- Stats dashboard -->
      <div
        class="mb-6 rounded-2xl p-5 border transition-colors duration-300"
        :class="
          dark
            ? 'bg-[#111111] border-[#1a1a1a]'
            : 'bg-white border-gray-200 shadow-sm'
        "
      >
        <div class="flex items-center justify-between mb-4">
          <h2
            class="text-xl font-bold"
            :class="dark ? 'text-white' : 'text-gray-900'"
          >
            {{ selectedCompany }}
          </h2>
          <div class="text-right">
            <span class="text-2xl font-bold text-emerald-400">{{
              solvedCount
            }}</span>
            <span class="text-lg text-slate-500">
              / {{ currentProblems.length }}</span
            >
          </div>
        </div>

        <div class="flex items-center gap-6">
          <!-- Ring -->
          <div class="relative w-28 h-28 flex-shrink-0">
            <svg class="w-full h-full -rotate-90" viewBox="0 0 100 100">
              <circle
                cx="50"
                cy="50"
                r="42"
                :stroke="dark ? '#1a1a1a' : '#e5e7eb'"
                stroke-width="10"
                fill="none"
              />
              <circle
                cx="50"
                cy="50"
                r="42"
                stroke="url(#progressGrad)"
                stroke-width="10"
                fill="none"
                stroke-linecap="round"
                :stroke-dasharray="2 * Math.PI * 42"
                :stroke-dashoffset="
                  2 * Math.PI * 42 * (1 - solvedPercent / 100)
                "
                class="transition-all duration-700 ease-out"
              />
              <defs>
                <linearGradient
                  id="progressGrad"
                  x1="0%"
                  y1="0%"
                  x2="100%"
                  y2="0%"
                >
                  <stop offset="0%" stop-color="#34d399" />
                  <stop offset="100%" stop-color="#06b6d4" />
                </linearGradient>
              </defs>
            </svg>
            <div
              class="absolute inset-0 flex flex-col items-center justify-center"
            >
              <span
                class="text-xl font-bold"
                :class="dark ? 'text-white' : 'text-gray-900'"
                >{{ solvedPercent }}%</span
              >
            </div>
          </div>

          <!-- Difficulty bars -->
          <div class="flex-1 space-y-3">
            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="text-green-400 font-semibold">Easy</span>
                <span :class="dark ? 'text-slate-400' : 'text-gray-500'"
                  >{{ solvedByDifficulty.easy }} / {{ counts.easy }}</span
                >
              </div>
              <div
                class="h-2 rounded-full overflow-hidden"
                :class="dark ? 'bg-[#1a1a1a]' : 'bg-gray-200'"
              >
                <div
                  class="h-full bg-green-500 rounded-full transition-all duration-500"
                  :style="{ width: diffPercent('Easy') + '%' }"
                ></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="text-yellow-400 font-semibold">Medium</span>
                <span :class="dark ? 'text-slate-400' : 'text-gray-500'"
                  >{{ solvedByDifficulty.medium }} / {{ counts.medium }}</span
                >
              </div>
              <div
                class="h-2 rounded-full overflow-hidden"
                :class="dark ? 'bg-[#1a1a1a]' : 'bg-gray-200'"
              >
                <div
                  class="h-full bg-yellow-500 rounded-full transition-all duration-500"
                  :style="{ width: diffPercent('Medium') + '%' }"
                ></div>
              </div>
            </div>
            <div>
              <div class="flex justify-between text-xs mb-1">
                <span class="text-red-400 font-semibold">Hard</span>
                <span :class="dark ? 'text-slate-400' : 'text-gray-500'"
                  >{{ solvedByDifficulty.hard }} / {{ counts.hard }}</span
                >
              </div>
              <div
                class="h-2 rounded-full overflow-hidden"
                :class="dark ? 'bg-[#1a1a1a]' : 'bg-gray-200'"
              >
                <div
                  class="h-full bg-red-500 rounded-full transition-all duration-500"
                  :style="{ width: diffPercent('Hard') + '%' }"
                ></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Problem table -->
      <div
        class="rounded-xl border overflow-hidden transition-colors duration-300"
        :class="
          dark
            ? 'bg-[#111111] border-[#1a1a1a]'
            : 'bg-white border-gray-200 shadow-sm'
        "
      >
        <div
          class="grid grid-cols-[44px_50px_1fr_90px_60px] gap-2 px-4 py-2.5 text-[11px] font-semibold uppercase tracking-wider border-b"
          :class="
            dark
              ? 'text-slate-500 border-[#1a1a1a]'
              : 'text-gray-400 border-gray-100 bg-gray-50'
          "
        >
          <span></span>
          <span>#</span>
          <span>Title</span>
          <span>Difficulty</span>
          <span>Freq</span>
        </div>

        <div
          v-for="p in filteredProblems"
          :key="p.id"
          class="grid grid-cols-[44px_50px_1fr_90px_60px] gap-2 px-4 py-2.5 items-center border-b transition-all duration-200"
          :class="[
            dark ? 'border-slate-700/20' : 'border-gray-100',
            solvedSet.has(p.id)
              ? dark
                ? 'bg-emerald-500/5 opacity-50'
                : 'bg-green-50 opacity-50'
              : dark
                ? 'hover:bg-slate-700/20'
                : 'hover:bg-gray-50',
          ]"
        >
          <div class="flex justify-center">
            <button
              @click="toggleSolved(p.id)"
              class="w-6 h-6 rounded-lg border-2 flex items-center justify-center text-xs cursor-pointer transition-all duration-200"
              :class="
                solvedSet.has(String(p.id))
                  ? 'bg-emerald-500 border-emerald-500 text-white scale-110'
                  : 'border-slate-600 text-transparent hover:border-emerald-400 hover:scale-105'
              "
            >
              ✓
            </button>
          </div>

          <span
            class="font-mono text-xs"
            :class="dark ? 'text-slate-500' : 'text-gray-400'"
            >{{ p.id }}</span
          >

          <a
            :href="`https://leetcode.com/problems/${p.slug}/`"
            target="_blank"
            class="text-sm truncate transition-colors"
            :class="
              solvedSet.has(p.id)
                ? dark
                  ? 'text-slate-400 line-through decoration-slate-600'
                  : 'text-gray-400 line-through decoration-gray-300'
                : dark
                  ? 'text-blue-400 hover:text-blue-300'
                  : 'text-blue-600 hover:text-blue-500'
            "
            >{{ p.title }}</a
          >

          <span
            class="text-xs font-medium px-2 py-0.5 rounded-full w-fit"
            :class="{
              'bg-green-500/10 text-green-400': p.difficulty === 'Easy',
              'bg-yellow-500/10 text-yellow-400': p.difficulty === 'Medium',
              'bg-red-500/10 text-red-400': p.difficulty === 'Hard',
            }"
            >{{ p.difficulty }}</span
          >

          <div
            class="w-10 h-1.5 rounded-full overflow-hidden"
            :class="dark ? 'bg-slate-800' : 'bg-gray-200'"
          >
            <div
              class="h-full bg-blue-500 rounded-full"
              :style="{ width: freqPercent(p.frequency) + '%' }"
            ></div>
          </div>
        </div>

        <div
          v-if="filteredProblems.length === 0"
          class="text-center py-12 text-sm"
          :class="dark ? 'text-slate-600' : 'text-gray-400'"
        >
          No problems match your filters.
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { getProgress, saveProgress, clearToken, getToken } from "./api";
import AuthForm from "./components/AuthForm.vue";
import data from "./data/problems.json";

const user = ref(null);
const username = ref('');
const selectedCompany = ref(data[0]?.company || "");
const selectedDifficulties = ref(new Set());
const selectedTopics = ref(new Set());
const sortBy = ref("frequency");
const showResetConfirm = ref(false);
const dark = ref(localStorage.getItem("lc-theme") !== "light");
const openDropdown = ref(null);

// Check auth state on mount
onMounted(() => {
  const token = getToken()
  if (token) {
    user.value = { authenticated: true }
    loadUserData()
  }
});

// Handle authentication - set user and load data
async function handleAuthenticated() {
  user.value = { authenticated: true }
  await loadUserData()
}

// Load user data from API
async function loadUserData() {
  try {
    console.log('Loading user data...')
    const data = await getProgress();
    console.log('Progress loaded:', data)
    if (data.solvedProblems) {
      // Create new Set to force reactivity
      solvedSet.value = new Set(data.solvedProblems);
      console.log('Solved problems restored:', Array.from(solvedSet.value))
    }
  } catch (err) {
    console.error("Error loading user data:", err);
  }
}

// Save solved problems to API
async function saveSolvedToAPI() {
  if (!user.value) return;
  try {
    console.log('Saving progress:', Array.from(solvedSet.value))
    await saveProgress(Array.from(solvedSet.value));
    console.log('Progress saved successfully')
  } catch (err) {
    console.error("Error saving data:", err);
  }
}

// Logout
async function handleLogout() {
  try {
    clearToken();
    user.value = null;
    username.value = '';
    // Clear local data
    selectedDifficulties.value = new Set();
    selectedTopics.value = new Set();
    solvedSet.value = new Set();
  } catch (err) {
    console.error("Error logging out:", err);
  }
}

function toggleDifficulty(difficulty) {
  const s = new Set(selectedDifficulties.value);
  s.has(difficulty) ? s.delete(difficulty) : s.add(difficulty);
  selectedDifficulties.value = s;
}

function toggleTopic(topic) {
  const s = new Set(selectedTopics.value);
  s.has(topic) ? s.delete(topic) : s.add(topic);
  selectedTopics.value = s;
}

function toggleTheme() {
  dark.value = !dark.value;
  localStorage.setItem("lc-theme", dark.value ? "dark" : "light");
}

const solvedSet = ref(new Set());

function toggleSolved(id) {
  const s = new Set(solvedSet.value);
  const idStr = String(id);
  s.has(idStr) ? s.delete(idStr) : s.add(idStr);
  solvedSet.value = s;
  // Save to API (no localStorage)
  saveSolvedToAPI();
}

function resetProgress() {
  solvedSet.value = new Set();
  saveSolvedToAPI();
  showResetConfirm.value = false;
}

const companyNames = computed(() => data.map((c) => c.company));

const currentProblems = computed(() => {
  const entry = data.find((c) => c.company === selectedCompany.value);
  return entry ? entry.problems : [];
});

const topicsList = computed(() => {
  const topics = new Set();
  currentProblems.value.forEach((p) => {
    if (p.topics && Array.isArray(p.topics)) {
      p.topics.forEach((t) => topics.add(t));
    }
  });
  return ["All", ...Array.from(topics).sort()];
});

const totalForCompany = computed(() => currentProblems.value.length);

const filteredProblems = computed(() => {
  let list = [...currentProblems.value];

  // Filter by selected difficulties (if any selected, only show those)
  if (selectedDifficulties.value.size > 0) {
    list = list.filter((p) => selectedDifficulties.value.has(p.difficulty));
  }

  // Filter by selected topics (if any selected, only show those)
  if (selectedTopics.value.size > 0) {
    list = list.filter(
      (p) => p.topics && p.topics.some((t) => selectedTopics.value.has(t)),
    );
  }

  if (sortBy.value === "frequency") {
    list.sort((a, b) => a.frequency - b.frequency);
  } else {
    const order = { Easy: 0, Medium: 1, Hard: 2 };
    list.sort((a, b) => order[a.difficulty] - order[b.difficulty]);
  }

  return list;
});

const counts = computed(() => ({
  easy: currentProblems.value.filter((p) => p.difficulty === "Easy").length,
  medium: currentProblems.value.filter((p) => p.difficulty === "Medium").length,
  hard: currentProblems.value.filter((p) => p.difficulty === "Hard").length,
}));

const solvedCount = computed(
  () => currentProblems.value.filter((p) => solvedSet.value.has(String(p.id))).length,
);

const solvedCountGlobal = computed(() => solvedSet.value.size);

const solvedPercent = computed(() => {
  if (!currentProblems.value.length) return 0;
  return Math.round((solvedCount.value / currentProblems.value.length) * 100);
});

const solvedByDifficulty = computed(() => ({
  easy: currentProblems.value.filter(
    (p) => p.difficulty === "Easy" && solvedSet.value.has(String(p.id)),
  ).length,
  medium: currentProblems.value.filter(
    (p) => p.difficulty === "Medium" && solvedSet.value.has(String(p.id)),
  ).length,
  hard: currentProblems.value.filter(
    (p) => p.difficulty === "Hard" && solvedSet.value.has(String(p.id)),
  ).length,
}));

function diffPercent(diff) {
  const total = counts.value[diff.toLowerCase()];
  const solved = solvedByDifficulty.value[diff.toLowerCase()];
  return total ? Math.round((solved / total) * 100) : 0;
}

function freqPercent(rank) {
  if (totalForCompany.value <= 1) return 100;
  return Math.max(10, 100 - ((rank - 1) / (totalForCompany.value - 1)) * 90);
}

const motivationMessage = computed(() => {
  const pct = solvedPercent.value;
  if (pct === 0) return "🎯 Pick a problem and start grinding!";
  if (pct < 10) return "🌱 Every journey starts with a single commit";
  if (pct < 25) return "🔥 You're warming up — keep the momentum!";
  if (pct < 50) return "💪 Almost halfway — you're on fire!";
  if (pct < 75) return "🚀 Over halfway! The finish line is in sight";
  if (pct < 100) return "⭐ So close to 100%! Don't stop now";
  return "👑 YOU CLEARED THIS COMPANY. ABSOLUTE LEGEND.";
});

const motivationColor = computed(() => {
  const pct = solvedPercent.value;
  if (pct === 100) return "text-yellow-400 font-bold";
  if (pct >= 50) return "text-emerald-400";
  return "text-slate-400";
});
</script>
