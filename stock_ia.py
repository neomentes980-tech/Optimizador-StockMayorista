# ==========================================
# SISTEMA DE OPTIMIZACIÓN DE STOCK CON IA
# Autor: neomentes980-tech
# ==========================================

import json
import logging
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass

# --- Configuración de logging (registro de eventos con fecha/hora) ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

RUTA_INVENTARIO = Path("inventario.json")
RUTA_ALERTAS = Path("alertas_generadas.txt")


@dataclass
class Producto:
    nombre: str
    stock_actual: int
    stock_minimo: int

    @property
    def en_riesgo(self) -> bool:
        return self.stock_actual < self.stock_minimo

    @property
    def porcentaje_stock(self) -> float:
        return round((self.stock_actual / self.stock_minimo) * 100, 1)


def cargar_inventario(ruta: Path) -> list[Producto]:
    """Carga el inventario desde un archivo JSON, con manejo de errores."""
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    try:
        datos = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"El archivo JSON está corrupto o mal formado: {e}")
