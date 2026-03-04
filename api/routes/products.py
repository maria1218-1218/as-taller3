from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.database import get_db
from api.models.product import Product

router = APIRouter()

@router.get("/")
async def get_products(db: Session = Depends(get_db)):
    # TODO: Implementar obtener lista de productos
    products = db.query(Product).all()
    return products

@router.get("/{product_id}")
async def get_product(product_id: int, db: Session = Depends(get_db)):
    # TODO: Implementar obtener producto por ID
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return product

@router.post("/")
async def create_product(db: Session = Depends(get_db)):
    # TODO: Implementar crear producto (admin)
    return {"message": "Create product endpoint"}

@router.put("/{product_id}")
async def update_product(product_id: int, db: Session = Depends(get_db)):
    # TODO: Implementar actualizar producto
    return {"message": "Update product endpoint"}

@router.delete("/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    # TODO: Implementar eliminar producto
    return {"message": "Delete product endpoint"}
