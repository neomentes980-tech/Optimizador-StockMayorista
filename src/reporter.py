import csv
import logging
from datetime import datetime
from src.models import Alerta

logger = logging.getLogger(__name__)


def generar_reporte_txt(alertas: list[Alerta], ruta: str = "reports/alertas_generadas.txt"):
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(f"Reporte generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        archivo.write(f"Total de alertas: {len(alertas)}\n\n")
        for alerta in alertas:
            archivo.write(alerta.mensaje() + "\n\n")
    logger.info(f"Reporte TXT guardado en {ruta}")


def generar_reporte_csv(alertas: list[Alerta], ruta: str = "reports/alertas_generadas.csv"):
    with open(ruta, "w", encoding="utf-8", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([
            "SKU", "Producto", "Stock actual", "Stock mínimo",
            "Días cobertura", "Punto reorden", "Cantidad sugerida", "Criticidad"
        ])
        for alerta in alertas:
            p = alerta.producto
            writer.writerow([
                p.sku, p.nombre, p.stock_actual, p.stock_minimo,
                p.dias_cobertura, p.punto_reorden, p.cantidad_sugerida, p.nivel_criticidad
            ])
    logger.info(f"Reporte CSV guardado en {ruta}")
