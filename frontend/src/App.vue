<template>
  <div class="site-shell" @mousemove="moveCursor">
    <div class="custom-cursor" :style="cursorStyle" />

    <header class="frame edge-reveal">
      <p class="kicker">ABRAR // FULL-STACK</p>
      <nav aria-label="Primary">
        <a href="#about">About</a>
        <a href="#experiences">Experiences</a>
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

      <section id="about" class="frame about-wrap reveal-left">
        <h2>About Me</h2>
        <p class="about-lead">

I'm a final-year B.E. student at BITS Pilani, Hyderabad, passionate about building production AI systems that solve real problems. Despite my Civil Engineering background, I taught myself backend development and AI/ML over the past two years and I've shipped production systems to prove it. I specialize in multi-agent LLM workflows, RAG pipelines, and scalable backend infrastructure. I thrive at the intersection of technical depth and business impact, and I'm always curious about how things work under the hood.
        </p>
        <p>
          I work across LLMs, APIs, and data flows, with attention to performance, maintainability, and
          features that solve real workflow problems.
        </p>
      </section>

      <section id="experiences" class="frame experience-wrap reveal-right">
        <h2>Experiences</h2>
        <div class="experience-list">
          <article class="experience-item">
            <p class="experience-period">2025 - July - Dec</p>
            <h3>Software Engineer Intern   -   Questt.Ai</h3>
            <p>
              I designed RESTful APIs supporting 50+ concurrent users with sub-200ms response times,
              orchestrated multi-agent LLM workflows using Langchain/Langgraph processing 500+ requests/day, and engineered document-processing systems achieving 95% extraction accuracy across 2500+ documents.
            </p>
            <p>
              <span class="learning-label">Learnings from Questt.Ai:</span>
              At Questt, I went deep on technical implementation building APIs, working with AI systems, solving complex data engineering challenges, and building forecasting models. But the communication and requirement-gathering skills from GMR Group helped me understand the 'why' behind what we were building, not just the 'how'.
            </p>
          </article>
          <article class="experience-item">
            <p class="experience-period">2024 - May-July</p>
            <h3>CSR Analyst   -   GMR Group</h3>
            <p>
              Monitoring and evaluating CSR projects to ensure they aligned with the company's
              social impact goals. Managing project data, which involved collecting, organizing, and analyzing
              information for comprehensive reporting. Engaging directly with stakeholders, including community members and partner
              organizations, to understand needs and support various initiatives. Preparing compliance reports for both management and regulatory bodies, ensuring
              adherence to CSR guidelines and regulations.
            </p>
            <p>
              <span class="learning-label">Learnings from GMR Group:</span>
              At GMR, I learned how to think about business value and communicate with non-technical
              stakeholders. I also gained exposure to working in a large organization, understanding compliance and managing large datasets skills that proved surprisingly relevant when I later moved into AI-focused roles.
            </p>
          </article>
        </div>
      </section>

      <section id="work" class="frame work-wrap">
        <ProjectRail :projects="store.projects" />
      </section>

      <section id="process" class="frame process-wrap reveal-right">
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
          <a href="https://github.com/rarba17" target="_blank" rel="noreferrer">GitHub</a>
          <a href="https://www.linkedin.com/in/mohammed-abrar-ahmed-052a5725a/" target="_blank" rel="noreferrer">LinkedIn</a>
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
  try {
    await Promise.all([store.fetchProjects(), store.fetchArticles()]);
  } catch (error) {
    console.error("Error fetching store data:", error);
    // Continue even if fetch fails - reveal animations should still work
  }

  // Use setTimeout to ensure DOM is fully rendered before setting up observer
  setTimeout(() => {
    try {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("in-view");
              // Unobserve after animation to improve performance
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1, rootMargin: "50px" }
      );

      const revealElements = document.querySelectorAll(
        ".reveal-left, .reveal-right, .reveal-spin, .reveal-clip, .edge-reveal"
      );

      revealElements.forEach((el) => {
        observer.observe(el);

        // For elements already in view on page load, trigger animation immediately
        if (el.getBoundingClientRect().top < window.innerHeight) {
          el.classList.add("in-view");
          observer.unobserve(el);
        }
      });
    } catch (error) {
      console.error("Error setting up reveal animations:", error);
    }
  }, 100);
});
</script>
