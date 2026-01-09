const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

mongoose.connect(process.env.MONGO_URI);

app.use("/inscription", require("./routes/inscription"));

app.listen(10000, () => console.log("Server running"));
