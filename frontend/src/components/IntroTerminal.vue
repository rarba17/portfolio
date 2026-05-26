<template>
  <section class="intro-shell reveal-left">
    <p class="text-xs tracking-[0.12em] uppercase opacity-70">Session log</p>
    <pre class="terminal">{{ visibleText }}<span class="cursor">_</span></pre>
    <p class="mt-4 max-w-xl text-sm leading-relaxed opacity-90">
      I build systems that feel intentional under pressure: fast APIs, tactile interfaces, and tools
      that help teams decide instead of just display.
    </p>
  </section>
</template>

<script setup>
import { onMounted, ref } from "vue";

const snippet = `const work = {
  medium: ["code", "copy", "motion"],
  goal: "make complexity readable",
  default: "ship with evidence"
};`;

const visibleText = ref("");

onMounted(() => {
  let idx = 0;
  const timer = setInterval(() => {
    visibleText.value = snippet.slice(0, idx);
    idx += 2;
    if (idx > snippet.length) clearInterval(timer);
  }, 18);
});
</script>
