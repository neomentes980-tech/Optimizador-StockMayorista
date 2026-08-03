import logging
from src.models import Producto, Alerta

logger = logging.getLogger(__name__)


def analizar_inventario(productos: list[Producto]) -> list[Alerta]:
    alertas = []
    for producto in productos:
        if producto.stock_actual < producto.punto_reorden:
            alertas.append(Alerta(producto))
            logger.warning(f"{producto.nivel_criticidad} - {producto.nombre}")

    logger.info(f"Se encontraron {len(alertas)} producto(s) en riesgo")
    return alertas
