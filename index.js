const express = require("express");
const { executePy } = require("./executePy");
const { generateFile } = require("./generateFile");
const cors = require("cors");
const app = express();

app.use(cors());

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

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

app.listen(process.env.PORT, () => {
  console.log(`Listening on port 5000!`);
});
