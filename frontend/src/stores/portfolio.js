import { defineStore } from "pinia";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "";

export const usePortfolioStore = defineStore("portfolio", {
  state: () => ({
    projects: [],
    articles: [],
    loadingProjects: false,
    loadingArticles: false,
    sendingMessage: false,
    contactStatus: ""
  }),
  actions: {
    async fetchProjects() {
      this.loadingProjects = true;
      try {
        const res = await fetch(`${API_BASE}/api/projects`);
        if (!res.ok) throw new Error("Failed to fetch projects");
        this.projects = await res.json();
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
