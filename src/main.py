import logging
from src.loader import cargar_inventario
from src.analyzer import analizar_inventario
from src.reporter import generar_reporte_txt, generar_reporte_csv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    logger.info("Iniciando sistema de optimización de stock...")
    productos = cargar_inventario()
    alertas = analizar_inventario(productos)

    if alertas:
        generar_reporte_txt(alertas)
        generar_reporte_csv(alertas)
        print(f"\n⚠️  Se encontraron {len(alertas)} producto(s) en riesgo. Ver reportes en /reports")
    else:
        print("\n✅ Todo el inventario está dentro de niveles normales.")


if __name__ == "__main__":
    main()
