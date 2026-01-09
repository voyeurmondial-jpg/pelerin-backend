const mongoose = require("mongoose");

const PelerinSchema = new mongoose.Schema({
  statut_vocationnel: String,
  nom: String,
  prenom: String,
  date_naissance: Date,
  numero: String,
  email: String,
  diocese: String,
  paroisse: String,
  createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model("Pelerin", PelerinSchema);
