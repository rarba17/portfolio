<template>
  <div class="site-shell" @mousemove="moveCursor">
    <div class="custom-cursor" :style="cursorStyle" />

    <header class="frame edge-reveal">
      <p class="kicker">ABRAR // FULL-STACK</p>
      <nav aria-label="Primary">
        <a href="#work">Work</a>
        <a href="#process">Process</a>
        <a href="#connect">Connect</a>
      </nav>
    </header>

    <main>
      <section class="frame intro-wrap">
        <IntroTerminal />
        <aside class="quote reveal-spin">
          <p>
            “The interface is not the decoration around data. It is the argument for how to act on it.”
          </p>
        </aside>
      </section>

      <section id="work" class="frame work-wrap">
        <ProjectRail :projects="store.projects" />
      </section>

      <section id="process" class="frame process-wrap reveal-clip">
        <h2>Process</h2>
        <p>
          I start with workflows, not components. First: where decisions happen and who is blocked.
          Then I shape data contracts and interaction states together, so backend and frontend evolve as
          one product surface.
        </p>
        <p>
          I choose constraints early: latency budgets, observability points, error boundaries, and failure
          messaging. That keeps polish honest and makes the system easier to grow without rewrites.
        </p>
        <!-- Intentional overlap: this "field note" breaks the regular flow to avoid template-like page rhythm. -->
        <div class="field-note">
          <span>Field note:</span> Ship explainability, not just speed.
        </div>
      </section>

      <section id="connect" class="frame connect-wrap reveal-left">
        <h2>Contact / Connect</h2>
        <p class="lead">
          Best channel is email. Social links stay open if that fits your workflow better.
        </p>
        <div class="links-row">
          <button type="button" @click="copyEmail">Copy Email</button>
          <a href="https://github.com/yourname" target="_blank" rel="noreferrer">GitHub</a>
          <a href="https://linkedin.com/in/yourname" target="_blank" rel="noreferrer">LinkedIn</a>
          <a href="/api/resume">Download Resume</a>
        </div>

        <form class="contact-form" @submit.prevent="submitContact">
          <label>
            <span>Name</span>
            <input v-model="form.name" name="name" autocomplete="name" required />
          </label>
          <label>
            <span>Email</span>
            <input v-model="form.email" type="email" name="email" autocomplete="email" required />
          </label>
          <label>
            <span>Message</span>
            <textarea v-model="form.message" name="message" rows="4" required />
          </label>
          <button type="submit" :disabled="store.sendingMessage">
            {{ store.sendingMessage ? "Sending..." : "Send Note" }}
          </button>
          <p class="status">{{ statusText }}</p>
        </form>
      </section>
    </main>
  </div>
</template>

<script setup>
import { computed, onMounted, reactive, ref } from "vue";
import IntroTerminal from "./components/IntroTerminal.vue";
import ProjectRail from "./components/ProjectRail.vue";
import { usePortfolioStore } from "./stores/portfolio";

const store = usePortfolioStore();
const form = reactive({
  name: "",
  email: "",
  message: ""
});

const cursor = ref({ x: 0, y: 0 });
const copied = ref(false);

const cursorStyle = computed(() => ({
  transform: `translate(${cursor.value.x}px, ${cursor.value.y}px)`
}));

const statusText = computed(() => {
  if (copied.value) return "Email copied.";
  return store.contactStatus;
});

function moveCursor(event) {
  cursor.value = { x: event.clientX, y: event.clientY };
}

async function copyEmail() {
  try {
    await navigator.clipboard.writeText("hello@yourname.dev");
    copied.value = true;
    setTimeout(() => (copied.value = false), 1200);
  } catch (_error) {
    copied.value = false;
  }
}

async function submitContact() {
  const payload = new FormData();
  payload.append("name", form.name);
  payload.append("email", form.email);
  payload.append("message", form.message);
  await store.submitContact(payload);
  if (store.contactStatus === "Message sent.") {
    form.name = "";
    form.email = "";
    form.message = "";
  }
}

onMounted(async () => {
  await Promise.all([store.fetchProjects(), store.fetchArticles()]);
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) entry.target.classList.add("in-view");
      });
    },
    { threshold: 0.25 }
  );
  document
    .querySelectorAll(".reveal-left, .reveal-right, .reveal-spin, .reveal-clip, .edge-reveal")
    .forEach((el) => observer.observe(el));
});
</script>
