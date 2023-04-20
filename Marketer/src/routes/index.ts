import {Router} from 'express';
import offersRoutes from './api/offers'

const router = Router();

router.use('/offers', offersRoutes);

export default router;