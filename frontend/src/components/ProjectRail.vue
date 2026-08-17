<template>
  <section class="work-shell">
    <h2>Selected Work</h2>
    <p class="work-lead">Each project is production-minded, constraint-tested, and outcome-oriented.</p>
    <p v-if="usingFallback" class="fallback-note">
      Showing local preview data because the API is unreachable.
    </p>

    <div class="project-grid" aria-label="Selected projects">
      <article
        v-for="(project, index) in projects"
        :key="project.id"
        :class="['project-card', `mood-${project.mood}`]"
      >
        <p class="project-index"></p>
        <div class="card-top">
          <h3>{{ project.title }}</h3>
          <p class="role">{{ project.role }}</p>
        </div>

        <p class="description">{{ project.description }}</p>

        <ul class="stack" aria-label="Project stack">
          <li v-for="item in project.stack" :key="item">{{ item }}</li>
        </ul>

        <div class="card-links">
          <a :href="project.live_url" target="_blank" rel="noopener noreferrer">Live →</a>
          <a :href="project.github_url" target="_blank" rel="noopener noreferrer">GitHub →</a>
        </div>
      </article>

      <article v-if="loading" class="project-card project-placeholder">
        <p class="project-index">…</p>
        <h3>Loading projects</h3>
        <p class="description">Fetching latest work from the portfolio API.</p>
      </article>

      <article v-else-if="!projects.length" class="project-card project-placeholder">
        <p class="project-index">00.</p>
        <h3>No projects loaded</h3>
        <p class="description">
          Could not load data from <code>/api/projects</code>. Check backend/API base config and refresh.
        </p>
      </article>
    </div>
  </section>
</template>

<script setup>
defineProps({
  loading: {
    type: Boolean,
    default: false
  },
  usingFallback: {
    type: Boolean,
    default: false
  },
  projects: {
    type: Array,
    default: () => []
  }
});
</script>
