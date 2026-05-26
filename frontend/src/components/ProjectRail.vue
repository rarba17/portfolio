<template>
  <section class="reveal-right">
    <div class="section-head">
      <h2>Selected Work</h2>
      <p class="opacity-80 text-sm">Drag sideways or scroll. Each tile is a real delivery with constraints.</p>
    </div>
    <div class="project-rail" aria-label="Selected projects">
      <article v-for="project in projects" :key="project.id" :class="['project-panel', `mood-${project.mood}`]">
        <div class="panel-top">
          <h3>{{ project.title }}</h3>
          <p class="role">{{ project.role }}</p>
        </div>
        <p class="description">{{ project.description }}</p>
        <ul class="stack">
          <li v-for="item in project.stack" :key="item">{{ item }}</li>
        </ul>
        <div class="panel-links">
          <a :href="project.live_url" target="_blank" rel="noreferrer">Live</a>
          <a :href="project.github_url" target="_blank" rel="noreferrer">GitHub</a>
        </div>
      </article>
    </div>
  </section>
</template>

<script setup>
defineProps({
  projects: {
    type: Array,
    default: () => []
  }
});
</script>
