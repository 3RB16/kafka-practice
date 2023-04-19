import dotenv from 'dotenv';
import { Pool } from 'pg';

dotenv.config();

const {
    PG_HOST,
    PG_DB,
    PG_USER,
    PG_PASS,
    NODE_ENV,
    PG_DB_TEST,
    PEPPER,
    SALT
} = process.env;
export const salt = SALT;
export const pepper = PEPPER;
let client: Pool = new Pool();
console.log(NODE_ENV);
if (NODE_ENV == 'dev') {
    client = new Pool({
        host: PG_HOST,
        database: PG_DB,
        user: PG_USER,
        password: PG_PASS,
    });
}
if (NODE_ENV == 'test') {
    client = new Pool({
        host: PG_HOST,
        database: PG_DB_TEST,
        user: PG_USER,
        password: PG_PASS
    });
}


export default client;
