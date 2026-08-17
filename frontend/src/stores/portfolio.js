import { defineStore } from "pinia";
import { FALLBACK_PROJECTS } from "../data/fallbackProjects";

function resolveApiBase() {
  if (import.meta.env.VITE_API_BASE_URL) return import.meta.env.VITE_API_BASE_URL;
  if (typeof window === "undefined") return "";

  const { protocol, hostname, port } = window.location;

  if (port === "5173" || port === "4173") {
    return `${protocol}//${hostname}:8000`;
  }

  return "";
}

const API_BASE = resolveApiBase();

async function fetchFromCandidates(path) {
  const sameOrigin = path;
  const configuredBase = API_BASE ? `${API_BASE}${path}` : null;
  const host = typeof window !== "undefined" ? window.location.hostname : "localhost";
  const fallbacks = [
    `${window.location.protocol}//${host}:8000${path}`,
    `${window.location.protocol}//${host}:8001${path}`
  ];

  const candidates = [sameOrigin, configuredBase, ...fallbacks].filter(Boolean);

  for (const url of candidates) {
    try {
      const res = await fetch(url);
      if (res.ok) {
        return await res.json();
      }
    } catch (_error) {
      // try next candidate
    }
  }

  throw new Error(`All API candidates failed for ${path}`);
}

export const usePortfolioStore = defineStore("portfolio", {
  state: () => ({
    projects: [],
    articles: [],
    loadingProjects: false,
    loadingArticles: false,
    sendingMessage: false,
    contactStatus: "",
    usingProjectFallback: false
  }),
  actions: {
    async fetchProjects() {
      this.loadingProjects = true;
      this.usingProjectFallback = false;
      try {
        this.projects = await fetchFromCandidates("/api/projects");
      } catch (error) {
        this.projects = FALLBACK_PROJECTS;
        this.usingProjectFallback = true;
        console.error("Error fetching projects:", error);
      } finally {
        this.loadingProjects = false;
      }
    },
    async fetchArticles() {
      this.loadingArticles = true;
      try {
        const res = await fetch(`${API_BASE}/api/articles`);
        if (!res.ok) throw new Error("Failed to fetch articles");
        this.articles = await res.json();
      } finally {
        this.loadingArticles = false;
      }
    },
    async submitContact(formData) {
      this.sendingMessage = true;
      this.contactStatus = "";
      try {
        const res = await fetch(`${API_BASE}/api/contact`, {
          method: "POST",
          body: formData
        });
        const body = await res.json();
        if (!res.ok) {
          const detail = body.detail;
          const msg = Array.isArray(detail)
            ? detail.map((e) => e.msg).join("; ")
            : detail || "Message failed";
          throw new Error(msg);
        }
        this.contactStatus = "Message sent.";
      } catch (error) {
        this.contactStatus = error.message;
      } finally {
        this.sendingMessage = false;
      }
    }
  }
});
