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

describe('test products endpoints', () => {
  // afterAll(async () => {
  //   // clean db
  //     const connection = await db.connect();
  //     const sql = `DELETE FROM products;
  //                 ALTER SEQUENCE products_id_seq RESTART WITH 1;\n`;
  //     await connection.query(sql);
  //     connection.release();
  // });

  it('should create new product', async () => {
    const response = await request
    .post('/api/offers/add')
    .send({
        name: 'product name',
        description: 'product description',
        price: 20,
    });
    expect(response.status).toBe(200);
});



})