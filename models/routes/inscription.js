const express = require("express");
const router = express.Router();
const Pelerin = require("../models/Pelerin");

router.post("/", async (req, res) => {
  try {
    await Pelerin.create(req.body);
    res.json({ success: true });
  } catch (e) {
    res.status(500).json({ success: false });
  }
});

module.exports = router;
