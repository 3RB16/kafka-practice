import { Router } from "express";
import { CreateController } from '../../controllers/OfferController'
import { DeleteOneController } from '../../controllers/OfferController'
import { DeleteAllController } from '../../controllers/OfferController'
const router = Router();

router.post('/add', CreateController);
router.delete('/deleteall', DeleteAllController);
router.delete('/delete/:id',  DeleteOneController);

export default router;