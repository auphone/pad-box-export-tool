const axios = require("axios");
const fs = require("fs");
const path = require("path");

const urlRoot = "https://pad.skyozora.com/images/pets";
const dest = "./pets";

if (!fs.existsSync(dest)) {
  fs.mkdirSync(dest);
}

function sliceIntoChunks(arr, chunkSize) {
  const res = [];
  for (let i = 0; i < arr.length; i += chunkSize) {
    const chunk = arr.slice(i, i + chunkSize);
    res.push(chunk);
  }
  return res;
}

const lastId = 8188;
let id = 1;
(async () => {
  while (true) {
    if (id > lastId) {
      break;
    }
    const filename = `${id++}.png`;
    const cacheFilepath = path.join(dest, filename);
    try {
      if (fs.statSync(cacheFilepath)) {
        continue;
      }
    } catch (err) {}
    try {
      const response = await axios.get(`${urlRoot}/${filename}`, {
        responseType: "arraybuffer",
      });
      fs.writeFileSync(cacheFilepath, Buffer.from(response.data, "binary"));
    } catch (err) {
      console.error(err);
      return false;
    }
  }
})();
