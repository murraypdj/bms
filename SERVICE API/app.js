require('dotenv').config(); 
const express = require('express');
const app = express();

app.use((req, res, next) => {
  // Log request details
  console.log(`${req.method} ${req.url}`);
  console.log('Headers:', req.headers);
  console.log('Body:', req.body);

  next();
});


//validate API key
const validateApiKey = (req, res, next) => {
    const apiKey = req.headers['x-api-key'];
  
    // Compare key to expected key
    if (apiKey && apiKey === process.env.API_KEY) {
      next(); 
    } else {
      res.status(401).json({ error: 'Unauthorized' });
    }
  };
  
  // requiremiddleware for all routes
  app.use(validateApiKey);

// Generate random usage data
const generateUsageData = () => {
  const customers = [];

  for (let i = 1; i <= 10; i++) {
    const customer = {
      id: i + Math.floor(Math.random() * 1000),
      voip_usage: Math.floor(Math.random() * 1000),
      sms_usage: Math.floor(Math.random() * 1000),
      storage_usage: Math.floor(Math.random() * 1000)+'GB',
      subscription: ''
    };

    let randomNum = Math.floor(Math.random() * 2);
    if (randomNum === 0)  {
        customer.subscription = 'Standard'
    }
    else{
        customer.subscription = 'Premium'
    }

    customers.push(customer);
  }

  return customers;
};

// Define a route to get randomly generated customer usage data
app.get('/usage-data', (req, res) => {
  const usageData = generateUsageData();
  res.json(usageData);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
