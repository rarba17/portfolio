/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        parchment: "#F6F1E6",
        ink: "#1F2023",
        mustard: "#D9A62B",
        plum: "#4A2C53",
        rust: "#A7482F",
        slate: "#4D5A66"
      },
      fontFamily: {
        display: ["Fraunces", "Literata", "serif"],
        body: ["Space Grotesk", "Inter", "sans-serif"]
      },
      boxShadow: {
        "sketch-inset": "inset 0 0 0 2px rgba(31,32,35,0.08)"
      }
    }
  },
  plugins: []
};
