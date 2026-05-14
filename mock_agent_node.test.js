const request = require('supertest');
const app = require('./mock_agent_node');

describe('POST /run', () => {
  it('should return default values when no body is provided', async () => {
    const response = await request(app)
      .post('/run')
      .send({});

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('agent', 'unknown');
    expect(response.body).toHaveProperty('trace_id', 'DL-local');
    expect(response.body).toHaveProperty('status', 'OK');
    expect(response.body).toHaveProperty('ts');
  });

  it('should return provided agent and trace_id when body is provided', async () => {
    const response = await request(app)
      .post('/run')
      .send({ agent: 'test-agent', trace_id: 'test-trace' });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('agent', 'test-agent');
    expect(response.body).toHaveProperty('trace_id', 'test-trace');
    expect(response.body).toHaveProperty('status', 'OK');
    expect(response.body).toHaveProperty('ts');
  });

  it('should correctly handle partial body (only agent provided)', async () => {
    const response = await request(app)
      .post('/run')
      .send({ agent: 'test-agent' });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('agent', 'test-agent');
    expect(response.body).toHaveProperty('trace_id', 'DL-local');
    expect(response.body).toHaveProperty('status', 'OK');
    expect(response.body).toHaveProperty('ts');
  });

  it('should correctly handle partial body (only trace_id provided)', async () => {
    const response = await request(app)
      .post('/run')
      .send({ trace_id: 'test-trace' });

    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('agent', 'unknown');
    expect(response.body).toHaveProperty('trace_id', 'test-trace');
    expect(response.body).toHaveProperty('status', 'OK');
    expect(response.body).toHaveProperty('ts');
  });
});
