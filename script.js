try { require("dotenv").config(); } catch (e) {}
const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "index.html")));

app.get("/health", (req, res) =>
  res.json({ status: "ok", project: "Team J: Multilingual Voice Assistant", stack: "node" })
);

app.post("/api/transcribe", (req, res) => {
  // TODO: Audio file -> {text, language}
  res.status(501).json({ error: "Not implemented", todo: "Audio file -> {text, language}" });
});

app.post("/api/translate", (req, res) => {
  // TODO: Body: {text, target} -> {text}
  res.status(501).json({ error: "Not implemented", todo: "Body: {text, target} -> {text}" });
});

app.post("/api/speak", (req, res) => {
  // TODO: Body: {text, lang} -> audio
  res.status(501).json({ error: "Not implemented", todo: "Body: {text, lang} -> audio" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Team J server running on http://localhost:${PORT}`));
