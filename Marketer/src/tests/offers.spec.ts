import { Offer, OfferModel } from '../models/OfferModel';
import db from '../database';
import supertest from 'supertest'
import app from '../index'

// create a request object
const offerModel = new OfferModel();
const request = supertest(app)

describe('Test endpoint response', () => {
  it('test hello world endpoint', async () => {
    const response = await request.get('/')
    expect(response.status).toBe(200)
  })
})

describe('test offers endpoints', () => {
  it('should create new offer', async () => {
    const response = await request
    .post('/api/offers/add')
      .send({
        name: 'offer name',
        description: 'offer description',
        price: 20,
    });
    expect(response.status).toBe(200);
  });
  it('should delete offer', async () => {
    const response = await request
        .delete('/api/offers/delete/1')
    expect(response.status).toBe(200);
  });

  it('should delete all offers', async () => {
    const response = await request
        .delete('/api/offers/deleteall')
    expect(response.status).toBe(200);
  });


})