<template>
  <section class="intro-terminal">
    <p class="terminal-label">Session Log ✱</p>
    <pre class="terminal-content">{{ visibleText }}<span class="cursor">_</span></pre>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";

const snippet = `runbook = {
  "goal": "make complexity readable",
  "default": "ship with evidence",
  "systems": ["APIs", "agents", "data flows"]
}`;

const visibleText = ref("");

onMounted(() => {
  if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    visibleText.value = snippet;
    return;
  }

  let idx = 0;
  const timer = setInterval(() => {
    visibleText.value = snippet.slice(0, idx);
    idx += 2;
    if (idx > snippet.length) clearInterval(timer);
  }, 16);
});
</script>
