const express = require("express");
const { executePy } = require("./executePy");
const { generateFile } = require("./generateFile");
const cors = require("cors");
const app = express();
const port = process.env.PORT || 5000;

app.use(cors());

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.send("hewo world");
});

app.post("/run", async (req, res) => {
  const { language = "cpp", code } = req.body;

  if (code === undefined) {
    return res.status(400).json({ success: false, error: "Empty code body!" });
  }
  // need to generate a c++ file with content from the request
  try {
    const filepath = await generateFile(language, code);
    const output = await executePy(filepath);
    return res.json({ filepath, output });
  } catch (err) {
    res.status(500).json({ err });
  }
  // write into DB
});

app.listen(port, () => {
  console.log(`Listening on http://localhost:${port} `);
});
