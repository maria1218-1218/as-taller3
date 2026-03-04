from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.database import get_db
from api.models.cart import Cart, CartItem

router = APIRouter()

@router.get("/")
async def get_user_cart(db: Session = Depends(get_db)):
    # TODO: Implementar obtener carrito del usuario
    return {"message": "Get cart endpoint"}

@router.post("/items")
async def add_item_to_cart(db: Session = Depends(get_db)):
    # TODO: Implementar agregar item al carrito
    return {"message": "Add item to cart endpoint"}

@router.put("/items/{item_id}")
async def update_cart_item(item_id: int, db: Session = Depends(get_db)):
    # TODO: Implementar actualizar cantidad de item
    return {"message": "Update cart item endpoint"}

@router.delete("/items/{item_id}")
async def remove_item_from_cart(item_id: int, db: Session = Depends(get_db)):
    # TODO: Implementar remover item del carrito
    return {"message": "Remove item from cart endpoint"}

@router.delete("/")
async def clear_cart(db: Session = Depends(get_db)):
    # TODO: Implementar limpiar carrito
    return {"message": "Clear cart endpoint"}
