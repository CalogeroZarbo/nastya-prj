// Main application entry point
const express = require('express');
const _ = require('lodash');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json());

// Routes
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to Nastya Project',
    environment: 'development',
    timestamp: new Date().toISOString(),
  });
});

app.get('/api/test', (req, res) => {
  res.json({
    success: true,
    data: 'API is working!',
    utils: _.size({ a: 1, b: 2 }),
  });
});

// Export the app instance for testing
module.exports = app;

// Only start the server if this file is executed directly (not imported)
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });
}
