"""API principal de Tienda Ágora."""

from fastapi import FastAPI, HTTPException

from app.products import get_product, list_products
from app.version import API_NAME, API_VERSION

app = FastAPI(
    title=API_NAME,
    version=API_VERSION,
    description="API didáctica para el curso de CI/CD.",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Smoke endpoint para validar que la API responde."""
    return {"status": "fail"}


@app.get("/version")
def version() -> dict[str, str]:
    """Devuelve información básica de versión."""
    return {"name": API_NAME, "version": API_VERSION}


@app.get("/products")
def products() -> list[dict]:
    """Devuelve el catálogo de productos."""
    return list_products()


@app.get("/products/{product_id}")
def product_detail(product_id: int) -> dict:
    """Devuelve el detalle de un producto."""
    product = get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
