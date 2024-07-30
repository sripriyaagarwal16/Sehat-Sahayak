import express from 'express';
import cors from 'cors';
import mongoose from 'mongoose';
import bodyParser from 'body-parser';
import apiRoutes from './routes/api.js';


const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5000;

const apiRoutes = require('./routes/api.js');
app.use('/api', apiRoutes);

const mongoose = require('mongoose');

const mongoURI = 'mongodb+srv://yashika1334:SGp6tAYf5cXWsEkP@cluster0.dqs9ipg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';

mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));



app.use(bodyParser.json());
app.use(cors());



app.get('/', (req, res) => {
  res.send('Hello, World!');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
