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
      expect(response.body.environment).toBe('development');
    });
  });

  describe('GET /api/test', () => {
    it('should return test data', async () => {
      const response = await request(testApp).get('/api/test');
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data).toBe('API is working!');
      expect(response.body.utils).toBe(2); // lodash _.size({ a: 1, b: 2 }) returns 2
    });
  });

  describe('GET /api/test with query parameters', () => {
    it('should handle query parameters correctly', async () => {
      const response = await request(testApp).get('/api/test?test=1');
      expect(response.status).toBe(200);
      expect(response.body.success).toBe(true);
      expect(response.body.data).toBe('API is working!');
    });
  });

  describe('Error handling', () => {
    it('should return 404 for non-existent routes', async () => {
      const response = await request(testApp).get('/non-existent');
      expect(response.status).toBe(404);
    });
  });
});