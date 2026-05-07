const request = require('supertest');
const app = require('./mock_agent_node');

describe('POST /run', () => {
  it('should return agent and trace_id from request body', async () => {
    const res = await request(app)
      .post('/run')
      .send({ agent: 'test_agent', trace_id: 'test_trace' })
      .set('Accept', 'application/json');

    expect(res.status).toBe(200);
    expect(res.body.agent).toBe('test_agent');
    expect(res.body.trace_id).toBe('test_trace');
    expect(res.body.status).toBe('OK');
    expect(res.body.ts).toBeDefined();
  });

  it('should use default values if body is empty', async () => {
    const res = await request(app)
      .post('/run')
      .send({})
      .set('Accept', 'application/json');

    expect(res.status).toBe(200);
    expect(res.body.agent).toBe('unknown');
    expect(res.body.trace_id).toBe('DL-local');
    expect(res.body.status).toBe('OK');
    expect(res.body.ts).toBeDefined();
  });

  it('should use default values if body is not provided', async () => {
    const res = await request(app)
      .post('/run')
      .set('Accept', 'application/json');

    expect(res.status).toBe(200);
    expect(res.body.agent).toBe('unknown');
    expect(res.body.trace_id).toBe('DL-local');
    expect(res.body.status).toBe('OK');
    expect(res.body.ts).toBeDefined();
  });
});
