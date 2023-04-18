import { Request, Response, NextFunction } from 'express';
// import { Offer,OfferModel } from '../models/OfferModel';

// const productModel = new OfferModel;
export const CreateController = async (req: Request, res: Response,next:NextFunction) => {
    try {
        // console.log(req.body);
        // const offer:Offer=await OfferModel.createNewProduct(req.body)
        res.json({
            status: 'success',
            // data: { ...offer },
            message: 'product created successfully'
        });
    } catch (err) {
        next(err);
    }
}

export const DeleteOneController = async (req: Request, res: Response,next:NextFunction) => {
    try {
        const id: number = parseInt(req.params.id as string);
        //const deleteOne = await OfferModel.deleteById(id);
        res.json({
            //data:{deleteOne},
            message: 'products deleted successfully'
        })
    } catch(err) {
        next(err);
    }
}

export const DeleteAllController = async (req: Request, res: Response,next:NextFunction) => {
    try {
        // const deleteAll = await OfferModel.deleteAll();
        res.json({
            // data:{deleteAll},
            message: 'products deleted successfully'
        })
    } catch(err) {
        next(err);
    }
}