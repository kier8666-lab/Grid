const express = require('express');
const app = express();
app.use(express.json());
app.post('/run', (req,res)=>{
  const {agent='unknown', trace_id='DL-local'} = req.body || {};
  res.json({agent, trace_id, status:'OK', ts:new Date().toISOString()});
});
app.listen(8081, ()=>console.log('Mock Agent Node listening 8081'));
