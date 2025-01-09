const express = require('express');
const multer = require('multer');
const path = require('path');
const app = express();

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
      cb(null, './uploads')
    },
    filename: function (req, file, cb) {
      const uniqueName = `${Date.now()}-${file.originalname}`
      cb(null, uniqueName)
    }
  });
  
  const upload = multer({ 
    storage: storage, 
    limits: {fileSize: 1000000},
    fileFilter: (req, file, cb) => {
    // Accept only .pptx files
    const filetypes = /pptx/;
    const extname = filetypes.test(path.extname(file.originalname).toLowerCase());
    if (extname) {
        return cb(null, true);
    }
    cb(new Error('Only .pptx files are allowed!'));
    },
});
