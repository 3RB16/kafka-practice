import db from '../database';

export type Offer = {
    id?: number | undefined;
    name: string;
    description: string;
    price: number;
};

export class OfferModel {
    async createNewoffer(offer: Offer): Promise<Offer> {
        try {
            const connect = await db.connect();
            const sql = 'INSERT INTO offer (name,description,price) VALUES ($1,$2,$3) returning *';
            const result = await connect.query(sql, [
                offer.name,
                offer.description,
                offer.price,
            ])
            connect.release();
            return result.rows[0];
        } catch (err) {
            throw new Error(`can't create (${offer.name}): ${err.message}`);
        }
    }

    async deleteById(id: number): Promise<Offer> {
        try {
            const connection = await db.connect();
            const sql = 'DELETE FROM offer WHERE id=($1) RETURNING *';
            const result = await connection.query(sql, [id]);
            connection.release();
            return result.rows[0];
        } catch (err) {
            throw new Error(`Could not delete offer ${id}, ${err.message}`);
        }
    }

    async deleteAll(): Promise<Offer[]>{
        try {
            const connection = await db.connect();
            const sql = 'DELETE FROM offer RETURNING *';
            const result = await connection.query(sql);
            connection.release();
            return result.rows;
        } catch (err) {
            throw new Error(`couldn't retrieving offer ${err.message}`);
        }
    }

}