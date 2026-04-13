const request = require('supertest');
const app = require('../src/index');

// Create a test server instance without starting it
const testApp = app;

describe('API Tests', () => {
  describe('GET /', () => {
    it('should return welcome message', async () => {
      const response = await request(testApp).get('/');
      expect(response.status).toBe(200);
      expect(response.body.message).toBe('Welcome to Nastya Project');
    });
  });

  describe('GET /api/test', () => {
    it('should return test data', async () => {
      const response = await request(testApp).get('/api/test');
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data).toBe('API is working!');
    });
  });
});