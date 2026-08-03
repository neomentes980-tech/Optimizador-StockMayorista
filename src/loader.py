import json
import logging
from src.models import Producto

logger = logging.getLogger(__name__)


def cargar_inventario(ruta: str = "data/inventario.json") -> list[Producto]:
    logger.info(f"Cargando inventario desde {ruta}")
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    productos = [Producto(**item) for item in datos]
    logger.info(f"Inventario cargado: {len(productos)} productos")
    return productos
