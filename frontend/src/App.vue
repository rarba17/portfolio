<template>
  <div class="site-shell">
    <div class="marquee-band" aria-hidden="true">
      <div class="marquee-track">
        HYDERABAD ✱ PRODUCTION AI ✱ BACKEND SYSTEMS ✱ RAG + AGENTS ✱ MCP ✱ HYDERABAD ✱
      </div>
    </div>

    <header class="site-header frame reveal-fade">
      <a class="brand" href="#about">◆ MOHAMMED ABRAR AHMED</a>
      <nav aria-label="Primary">
        <a
          v-for="item in navItems"
          :key="item.id"
          :href="item.href"
          :class="{ 'is-active': activeSection === item.id }"
          :aria-current="activeSection === item.id ? 'page' : undefined"
        >
          {{ item.label }}
        </a>
      </nav>
      <a class="resume-link" href="/api/resume">Resume ↗</a>
    </header>

    <main>
      <section id="about" class="frame hero-wrap reveal-up">
        <p class="catalog-line">◆ Portfolio · Open to Software Engineering + AI Engineering roles</p>
        <h1>
          SHIP<br />
          WITH EVIDENCE.
        </h1>

        <div class="hero-grid">
          <div class="hero-copy">
            <p>
              I’m a Recent Graduate from <b>BITS Pilani</b>, building production AI products that
              survive real constraints: latency, messy data, and evolving business requirements.
            </p>
            <p>
              I work across multi-agent LLM workflows, RAG, APIs, and backend infrastructure with a product
              lens focused on decision quality and operational reliability.
            </p>
            <div class="hero-actions">
              <a href="#work">View selected work</a>
              <a href="#connect">Contact</a>
            </div>
          </div>

          <aside class="hero-meta" aria-label="Profile facts">
            <p><span>Focus</span> Production AI + Backend</p>
            <p><span>Primary stack</span> FastAPI · LangChain · LangSmith · LangGraph · PostgreSQL · Redis · Celery · Node.js · Express.js · MongoDB · VectorDB's </p>
            <p><span>Current base</span> Hyderabad, India</p>
            <p><span>Best channel</span> Email</p>
          </aside>
        </div>

        <IntroTerminal />
      </section>



      <section id="experiences" class="frame experiences-wrap reveal-right">
        <h2>Experiences</h2>
        <div class="exp-list">
          <article class="exp-item">
            <p class="exp-index"> </p>
            <p class="experience-period">July 2025 — December 2025</p>
            <h3>Software Engineer Intern · Questt.Ai</h3>
            <ul>
              <li>Built REST APIs serving 50+ concurrent users at sub-200ms latency.</li>
              <li>Orchestrated LangChain/LangGraph workflows processing 500+ requests/day.</li>
              <li>Engineered document extraction pipelines at ~95% accuracy over 2,500+ files.</li>
            </ul>
          </article>

          <article class="exp-item">
            <p class="exp-index"> </p>
            <p class="experience-period">May 2024 — July 2024</p>
            <h3>CSR Analyst · GMR Group</h3>
            <ul>
              <li>Owned project monitoring/reporting workflows for compliance and impact visibility.</li>
              <li>Worked with stakeholders to translate field requirements into action plans.</li>
              <li>Developed business communication rigor now applied to AI product delivery.</li>
            </ul>
          </article>
        </div>
      </section>

      <section id="work" class="frame work-wrap reveal-up">
        <ProjectRail
          :projects="store.projects"
          :loading="store.loadingProjects"
          :using-fallback="store.usingProjectFallback"
        />
      </section>

      <section id="process" class="frame process-wrap reveal-left">
        <h2>Process</h2>
        <div class="process-list">
          <article>
            <p class="step">01</p>
            <h3>Map Bottlenecks</h3>
            <p>Identify blocked decisions, user friction, and risky handoffs first.</p>
          </article>
          <article>
            <p class="step">02</p>
            <h3>Define Contracts</h3>
            <p>Set API/data contracts, failure paths, and observability checkpoints early.</p>
          </article>
          <article>
            <p class="step">03</p>
            <h3>Ship in Slices</h3>
            <p>Release measurable increments, evaluate outcomes, and tighten reliability.</p>
          </article>
        </div>
      </section>

      <section id="connect" class="frame connect-wrap reveal-fade">
        <h2>Connect</h2>
        <p class="connect-lead">
          If you’re hiring for backend or AI systems, I’d love to contribute.
        </p>

        <div class="links-row">
          <button type="button" @click="copyEmail">Copy Email</button>
          <a href="https://github.com/rarba17" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a href="https://www.linkedin.com/in/mohammed-abrar-ahmed-052a5725a/" target="_blank" rel="noopener noreferrer">LinkedIn</a>
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
          <p class="status" role="status" aria-live="polite">{{ statusText }}</p>
        </form>
      </section>
    </main>

    <div class="marquee-band inverse" aria-hidden="true">
      <div class="marquee-track">
        ABRAR AHMED ◆ FASTAPI ◆ AGENTS ◆ RAG ◆ PRODUCTION SYSTEMS ◆ NODE.JS ◆
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onBeforeUnmount, onMounted, reactive, ref } from "vue";
import IntroTerminal from "./components/IntroTerminal.vue";
import ProjectRail from "./components/ProjectRail.vue";
import { usePortfolioStore } from "./stores/portfolio";

const store = usePortfolioStore();
const form = reactive({
  name: "",
  email: "",
  message: ""
});

const copied = ref(false);
const reduceMotion = ref(false);
const activeSection = ref("about");

const navItems = [
  { id: "about", label: "About", href: "#about" },
  { id: "experiences", label: "Experiences", href: "#experiences" },
  { id: "work", label: "Work", href: "#work" },
  { id: "process", label: "Process", href: "#process" },
  { id: "connect", label: "Connect", href: "#connect" }
];

let revealObserver;
let sectionObserver;

const statusText = computed(() => {
  if (copied.value) return "Email copied.";
  return store.contactStatus;
});

async function copyEmail() {
  try {
    await navigator.clipboard.writeText("mmaapril42@gmail.com");
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
  if (window.matchMedia) {
    reduceMotion.value = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  try {
    await Promise.all([store.fetchProjects(), store.fetchArticles()]);
  } catch (error) {
    console.error("Error fetching store data:", error);
  }

  const revealElements = document.querySelectorAll(".reveal-up, .reveal-left, .reveal-right, .reveal-fade");

  if (reduceMotion.value) {
    revealElements.forEach((element) => element.classList.add("in-view"));
  } else {
    revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("in-view");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.16, rootMargin: "24px" }
    );

    revealElements.forEach((element) => revealObserver.observe(element));
  }

  sectionObserver = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

      if (visible?.target?.id) {
        activeSection.value = visible.target.id;
      }
    },
    {
      threshold: [0.3, 0.5, 0.7],
      rootMargin: "-22% 0px -55% 0px"
    }
  );

  navItems.forEach((item) => {
    const section = document.getElementById(item.id);
    if (section) sectionObserver.observe(section);
  });
});

onBeforeUnmount(() => {
  if (revealObserver) revealObserver.disconnect();
  if (sectionObserver) sectionObserver.disconnect();
});
</script>
